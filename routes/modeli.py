from routes.ekstenzije import db
from flask_login import UserMixin

class User(UserMixin, db.Model):    # kreira model korisnika koji nasleđuje UserMixin i db.Model, što omogućava integraciju sa Flask-Login i SQLAlchemy.
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)