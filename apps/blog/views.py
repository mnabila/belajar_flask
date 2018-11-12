from flask import render_template
from .models import Article, post, Category
from apps.dashboard.models import Users

article_all = Article.query.filter_by(published=True).all()
category_all = Category.query.all()


def index():
    context = {
        "title": "Home",
        "heading": "Rumah Ilmu",
        "subheading": "Selamat datang di Rumah Ilmu",
        "articles": article_all,
        "category": category_all
    }
    return render_template("blog/index.html", **context)


def post(id):
    article = Article.query.filter_by(id=id).first()
    context = {
        "title": article.title,
        "heading": "Rumah Ilmu",
        "subheading": "Selamat datang di Rumah Ilmu",
        "article": article,
        "category": category_all
    }
    return render_template("blog/post.html", **context)


def tags(name):
    context = {
        "title": "Home",
        "heading": "Rumah Ilmu",
        "subheading": "Selamat datang di Rumah Ilmu",
        "articles": Category.query.filter_by(name=name).all(),
        "category": category_all
    }
    return render_template("blog/index.html", **context)


def author(uid):
    context = {
        "title": "About | Author",
        "heading": "Rumah Ilmu",
        "subheading": "Selamat datang di Rumah Ilmu",
        "user": Users.query.filter_by(id=uid).first()
    }
    return render_template("blog/author.html", **context)
