from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()   # inicijalizacija ekstenzije SQLAlchemy, koja omogućava rad sa bazom podataka u Flask aplikaciji.
login_manager = LoginManager()