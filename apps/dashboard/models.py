from apps import db
from flask_login import UserMixin


class Users(db.Model, UserMixin):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(50))
    bio = db.Column(db.Text, nullable=True)
    article = db.relationship("Article", backref="user", lazy=True)

