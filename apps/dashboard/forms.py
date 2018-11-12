from flask_wtf import FlaskForm
from wtforms import (StringField, PasswordField, SubmitField, BooleanField, TextAreaField, SelectMultipleField)
from wtforms.validators import DataRequired


class formLogin(FlaskForm):
    username = StringField(label="Username", validators=[
                           DataRequired(message="Username tidak boleh kosong")],)
    password = PasswordField(label="Password", validators=[
                             DataRequired(message="Password tidak boleh kosong")])
    remember = BooleanField(label="Remember user login")
    login = SubmitField()


class formArticle(FlaskForm):
    title = StringField(label="Judul")
    body = TextAreaField(label="body")
    category = TextAreaField(label="kategori")
    save = SubmitField()
    draft = SubmitField()
