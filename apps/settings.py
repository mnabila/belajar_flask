import os
from datetime import timedelta

# static folder for css, js, img, etc
STATIC_FOLDER = os.path.join(os.getcwd() + "/static")
TEMPLATES_FOLDER = os.path.join(os.getcwd() + "/templates")


# config flask webapps
class flaskConfig:
    DEBUG = True
    SECRET_KEY = '1234567890qwerty'
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:dani@127.0.0.1:3306/flask?unix_socket=/opt/lampp/var/mysql/mysql.sock"
    # SQLALCHEMY_DATABASE_URI = "sqlite:///db.sqlite3"
    PERMANENT_SESSION_LIFETIME = timedelta(minutes=5)
