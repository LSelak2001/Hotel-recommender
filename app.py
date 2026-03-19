from flask import Flask, render_template, request, redirect, url_for

import mysql.connector

app = Flask(__name__) # rutina za kreiranje aplikacije

# konekcija na bazu

konekcija = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="smestaj"
)
cursor = konekcija.cursor(dictionary=True)

#Početna stranica
@app.route("/")
def index():
    cursor.execute("SELECT * FROM hotel")
    hotel = cursor.fetchall()
    return render_template("index.html", hotel=hotel)

#Dodavanje smestaja
@app.route("/dodaj_smestaj", methods=["POST"])
def dodaj_smestaj():
    naziv = request.form["naziv"]
    adresa = request.form["adresa"]
    grad = request.form["grad"]
    kontinent = request.form["kontinent"]
    zvezdice = request.form["zvezdice"]
    ljubimci = request.form["ljubimci"]
    vrsta_smestaja = request.form["vrsta_smestaja"]
    obrok = request.form["obrok"]
    
    try:
        # 1) drzava
        cursor.execute("INSERT INTO drzava (naziv, kontinent) VALUES (%s, %s)", (naziv, kontinent))
        drzava_id = cursor.lastrowid
    
        # 2) grad
        cursor.execute("INSERT INTO grad (naziv, drzava_id) VALUES (%s, %s)", (grad, drzava_id))
        grad_id = cursor.lastrowid
    
        # 3) hotel
        cursor.execute(
        "INSERT INTO hotel (naziv, adresa, grad_id, zvezdice, ljubimci, vrsta_smestaja, obrok) VALUES (%s,%s,%s,%s,%s,%s,%s)",
        (naziv, adresa, grad_id, zvezdice, ljubimci, vrsta_smestaja, obrok)
        )
    
        konekcija.commit()
        return redirect(url_for("index"))
    except Exception:
        konekcija.rollback()
        raise

if __name__ == "__main__":  # program startuje app.py
    app.run(debug = True)  # Promeniti na kraju projekta na False, da se ne bi prikazivali detalji o greškama korisnicima.