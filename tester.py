from apps import db
from apps.dashboard.models import Users
from apps.blog.models import post, Article, Category, BlogSettings


db.create_all()
dani = Users(username="dani", password="dani", name="dani ardaniar")
horor = Category(name="horor")
aksi = Category(name="aksi")

db.session.add_all([dani, horor, aksi])
db.session.commit()

artikel1 = Article(title="satu", body="loremEsse ad cupidatat aliquip ut nostrud veniam esse laborum id enim eiusmod eiusmod in in.")
db.session.add(artikel1)
db.session.commit()

artikel1.user = dani
artikel1.category.append(aksi)
db.session.commit()

blog = BlogSettings(name="Rumah ilmu", description="website rumah ilmu")
db.session.add(blog)
db.session.commit()
