from apps import db
from datetime import datetime


post = db.Table("post",
                db.Column("id", db.Integer, primary_key=True),
                db.Column("article_id", db.Integer,
                          db.ForeignKey("article.id")),
                db.Column("category_id", db.Integer,
                          db.ForeignKey("category.id")),
                )


class Article(db.Model):
    __tablename__ = "article"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(300))
    body = db.Column(db.Text)
    pubDate = db.Column(db.DateTime, default=datetime.now())
    published = db.Column(db.Boolean, nullable=False, default=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    category = db.relationship("Category", secondary=post,
                               backref=db.backref("article", lazy="dynamic"))
    counter = db.relationship("Counters", backref="article", lazy=True)


class Category(db.Model):
    __tablename__ = "category"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))


class Counters(db.Model):
    __tablename__ = "counter"
    id = db.Column(db.Integer, primary_key=True)
    article_id = db.Column(db.Integer, db.ForeignKey('article.id'))
    count = db.Column(db.Integer, nullable=False, default=0)


class BlogSettings(db.Model):
    __tablename__ = "blog_settings"
    id=db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text)