from flask import Flask
from routes.hoteli import hoteli_bp
from routes.smestaj import smestaj_bp

app = Flask(__name__) # rutina za kreiranje aplikacije
app.register_blueprint(hoteli_bp)
app.register_blueprint(smestaj_bp)

if __name__ == "__main__":  # program startuje app.py
    app.run(debug = True)  # Promeniti na kraju projekta na False, da se ne bi prikazivali detalji o greškama korisnicima.