from flask import Blueprint, render_template, request, redirect, url_for
from config import cursor

hoteli_bp = Blueprint("hoteli", __name__)

@hoteli_bp.route("/")
def index():
    cursor.execute("""SELECT hotel.hotelID, hotel.naziv, hotel.adresa, hotel.zvezdice, hotel.ljubimci, hotel.vrsta_smestaja, hotel.obrok,
                        grad.naziv_grada AS grad_naziv
                    FROM hotel
                    JOIN grad ON hotel.gradID = grad.gradID
                    ORDER BY hotel.hotelID""")
    hoteli = cursor.fetchall()
    return render_template("hoteli.html", hoteli=hoteli)

@hoteli_bp.route("/filter", methods=["GET", "POST"])
def filter():
    if request.method == "GET":
        return render_template("filter.html")

    zvezdice = int(request.form.get("zvezdice")) if request.form.get("zvezdice") else None
    ljubimci = int(request.form.get("ljubimci")) if request.form.get("ljubimci") != "" else None
    vrsta_smestaja = request.form.get("vrsta_smestaja") or None
    obrok = request.form.get("obrok") or None

    query = """
        SELECT hotel.*, grad.naziv_grada AS grad_naziv
        FROM hotel
        JOIN grad ON hotel.gradID = grad.gradID
    """

    filters = []
    params = []

    if zvezdice:
        filters.append("hotel.zvezdice = %s")
        params.append(zvezdice)
    if ljubimci:
        filters.append("hotel.ljubimci = %s")
        params.append(ljubimci)
    if vrsta_smestaja:
        filters.append("hotel.vrsta_smestaja = %s")
        params.append(vrsta_smestaja)
    if obrok:
        filters.append("hotel.obrok = %s")
        params.append(obrok)

    if filters:
        query += " WHERE " + " AND ".join(filters)

    cursor.execute(query, params)
    hoteli = cursor.fetchall()
    return render_template("hoteli.html", hoteli=hoteli)