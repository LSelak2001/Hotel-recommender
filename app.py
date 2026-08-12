from flask import Flask
from routes.ekstenzije import db, login_manager
from routes.hoteli import hoteli_bp
from routes.smestaj import smestaj_bp
from routes.korisnik import korisnik_bp
from routes.modeli import User
from datetime import timedelta

app = Flask(__name__) # rutina za kreiranje aplikacije
app.config['SECRET_KEY'] = 'your-secret-key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root@localhost/smestaj'
app.config['REMEMBER_COOKIE_DURATION'] = timedelta(days=30)

db.init_app(app)    # inicijalizacija ekstenzije SQLAlchemy sa aplikacijom
login_manager.init_app(app)
login_manager.login_view = 'korisnik.login'

app.register_blueprint(hoteli_bp)
app.register_blueprint(smestaj_bp)
app.register_blueprint(korisnik_bp)

@login_manager.user_loader  # definiše funkciju za učitavanje korisnika
def load_user(user_id):
    return User.query.get(int(user_id))

if __name__ == "__main__":  # program startuje app.py
    with app.app_context():
        db.create_all()
    app.run(debug = True)  # Promeniti na kraju projekta na False, da se ne bi prikazivali detalji o greškama korisnicima.