from flask import (Blueprint, render_template, request,
                   url_for, jsonify, redirect, flash)
from flask_login import (login_user, logout_user, current_user, login_required)
from apps.settings import STATIC_FOLDER, TEMPLATES_FOLDER
from apps import lm, db
from .models import Users
from apps.blog.models import Article, Category, post
from .forms import formLogin, formArticle

bDashboard = Blueprint("dashboard", __name__,
                       static_folder=STATIC_FOLDER, template_folder=TEMPLATES_FOLDER)
lm.session_protection = "strong"


@lm.user_loader
def user_load(uid):
    return Users.query.get(int(uid))


@lm.unauthorized_handler
def unauthorized_callback():
    return redirect(url_for("dashboard.login"))


@bDashboard.route("/", methods=["POST", "GET"])
def login():
    form = formLogin()
    context = {
        "form": form,
    }
    if request.method == "POST":
        if form.validate_on_submit():
            user = Users.query.filter_by(
                username=form.username.data, password=form.password.data).first()
            if user:
                login_user(user)
                return redirect(url_for("dashboard.home"))
        else:
            flash("csrf_token hilang tong")
    elif request.method == "GET":
        if current_user.is_authenticated and current_user.username is not None:
            return redirect(url_for("dashboard.home"))
    return render_template("dashboard/login.html", **context)


@bDashboard.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("dashboard.login"))


@bDashboard.route("/home")
@login_required
def home():
    context = {
        "title": "Home",
        "current_user": current_user
    }
    return render_template("dashboard/index.html", **context)


@bDashboard.route("/article", methods=["GET", "POST"])
@login_required
def article():
    form = formArticle()
    option = request.args.get("option")
    label = request.args.get("label")
    status = request.args.get("status")
    action = request.args.get("action")
    context = {
        "form": form,
        "category": Category.query.all()
    }
    if request.method == "GET":
        if option == "new":
            context["title"] = "Artikel Baru"
            return render_template("dashboard/new_post.html", **context)
        elif option == "all" or option is None:
            if label is not None:
                print(label)
                context["articles"] = Category.query.filter_by(
                    name=label).first().article
            else:
                if status == "published":
                    context["articles"] = Article.query.filter_by(
                        published=True).all()
                    context["title"] = "Diterbitkan"
                elif status == "draft":
                    context["title"] = "Disimpan"
                    context["articles"] = Article.query.filter_by(
                        published=False).all()
            return render_template("dashboard/post.html", **context)

    elif request.method == "POST" and option == "new":
        if form.validate_on_submit():
            if form.save.data is True and form.draft.data is False:
                post = Article(title=form.title.data,
                               body=form.body.data, published=True)
                flash(
                    "<b>{t}</b> ditambahkan ke daftar Diterbitkan".format(t=post.title), category="succes")
            elif form.save.data is False and form.draft.data is True:
                post = Article(title=form.title.data,
                               body=form.body.data, published=False)
                flash(
                    "<b>{t}</b> ditambahkan ke daftar Disimpan".format(t=post.title), category="succes")
            user = Users.query.filter_by(
                username=current_user.username).first()
            post.user = user
            db.session.add(post)
            tags = str(form.category.data).split(",")
            for tag in tags:
                c = Category.query.filter_by(name=tag).first()
                if c.name is not None:
                    post.category.append(c)
            db.session.commit()
            return render_template("dashboard/new_post.html", **context)

@bDashboard.route("/category")
def category():
    pass