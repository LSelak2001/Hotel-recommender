import mysql.connector

konekcija = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="smestaj"
)
cursor = konekcija.cursor(dictionary=True, buffered=True)  # dictionary=True da bi se rezultati vraćali kao rečnici, buffered=True da bi se rezultati mogli ponovo koristiti