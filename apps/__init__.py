from flask import Flask, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from .settings import flaskConfig

app = Flask(__name__)
app.config.from_object(flaskConfig)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
lm = LoginManager(app=app)

# from apps.blog.urls import bBlog
# app.register_blueprint(bBlog, url_prefix="/blog")

# from apps.dashboard.views import bDashboard
# app.register_blueprint(bDashboard, url_prefix="/dashboard")
# db.create_all()

@app.route("/")
def index():
    return redirect(url_for("blog.index"))
