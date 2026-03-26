from flask import Blueprint, render_template, request, redirect, url_for
from config import cursor, konekcija

smestaj_bp = Blueprint("smestaj", __name__)

@smestaj_bp.route("/dodaj_smestaj", methods=["GET", "POST"])
def dodaj_smestaj():
    if request.method == "GET":
        return render_template("dodaj_smestaj.html")

    naziv = request.form["naziv"]
    adresa = request.form["adresa"]
    grad = request.form["grad"]
    drzava = request.form["drzava"]
    kontinent = request.form["kontinent"]
    zvezdice = request.form["zvezdice"]
    ljubimci = request.form["ljubimci"]
    vrsta_smestaja = request.form["vrsta_smestaja"]
    obrok = request.form["obrok"]
    
    try:
        # 1) drzava
        cursor.execute("INSERT INTO drzava (drzava, kontinent) VALUES (%s, %s)", (drzava, kontinent))
        drzava_id = cursor.lastrowid
    
        # 2) grad
        cursor.execute("INSERT INTO grad (naziv_grada, drzavaID) VALUES (%s, %s)", (grad, drzava_id))
        grad_id = cursor.lastrowid
    
        # 3) hotel
        cursor.execute(
        "INSERT INTO hotel (naziv, adresa, gradID, zvezdice, ljubimci, vrsta_smestaja, obrok) VALUES (%s,%s,%s,%s,%s,%s,%s)",
        (naziv, adresa, grad_id, zvezdice, ljubimci, vrsta_smestaja, obrok)
        )
    
        konekcija.commit()
        return redirect(url_for("hoteli.index"))
    except Exception:
        konekcija.rollback()
        raise

@smestaj_bp.route("/izmeni_smestaj/<int:hotel_id>", methods=["GET", "POST"])
def izmeni(hotel_id):
    if request.method == "GET":
        cursor.execute("""
            SELECT hotel.*, grad.naziv_grada, grad.gradID
            FROM hotel
            JOIN grad ON hotel.gradID = grad.gradID
            WHERE hotel.hotelID = %s
        """, (hotel_id,))
        hotel = cursor.fetchone()
        return render_template("izmeni_smestaj.html", hotel=hotel)

    # POST - save changes
    try:
        cursor.execute("""
            UPDATE hotel
            SET naziv=%s, adresa=%s, zvezdice=%s, ljubimci=%s, vrsta_smestaja=%s, obrok=%s
            WHERE hotelID=%s
        """, (
            request.form["naziv"],
            request.form["adresa"],
            request.form["zvezdice"],
            request.form["ljubimci"],
            request.form["vrsta_smestaja"],
            request.form["obrok"],
            hotel_id
        ))
        cursor.execute("UPDATE grad SET naziv_grada=%s WHERE gradID=%s",
                       (request.form["naziv_grada"], request.form["grad_id"]))
        konekcija.commit()
        return redirect(url_for("hoteli.index"))
    except Exception:
        konekcija.rollback()
        raise


@smestaj_bp.route("/obrisi/<int:hotel_id>", methods=["POST"])
def obrisi(hotel_id):
    try:
        cursor.execute("DELETE FROM hotel WHERE hotelID = %s", (hotel_id,))
        konekcija.commit()
        return redirect(url_for("hoteli.index"))
    except Exception:
        konekcija.rollback()
        raise