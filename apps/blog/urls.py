from flask import Blueprint
from . import views
from apps.settings import TEMPLATES_FOLDER, STATIC_FOLDER


bBlog = Blueprint("blog", __name__, static_folder=STATIC_FOLDER, template_folder=TEMPLATES_FOLDER)


bBlog.add_url_rule("/", "index", views.index)
bBlog.add_url_rule("/<int:id>", "post", views.post)
bBlog.add_url_rule("/tag/<string:name>", "tag", views.tags)
bBlog.add_url_rule("/author/<int:uid>", "author", views.author)
