from routes.ekstenzije import db
from flask_login import UserMixin

class User(UserMixin, db.Model):    # kreira model korisnika koji nasleđuje UserMixin i db.Model, što omogućava integraciju sa Flask-Login i SQLAlchemy.
    __tablename__ = 'korisnik'  # definiše ime tabele u bazi podataka za model korisnika
    id = db.Column('korisnikID', db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column('lozinka', db.String(255), nullable=False)
    role = db.Column('uloga', db.Enum('admin', 'korisnik'), default='korisnik', nullable=False)

    @property
    def is_admin(self):
        return self.role == 'admin'