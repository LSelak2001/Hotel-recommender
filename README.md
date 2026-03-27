# Hotel-recommender
Projekat za pravljenje aplikacije koja predlaže smeštaj korisnicima bazirano na određenim kriterijumima, poput lokacije,
da li primaju ljubimce i kako je uslužena hrana.

1. korak - Python: osnovne funkcije i testiranje funkcija (sa posebnim HTML kodom koji je samo u svrhi testiranja)
2. korak - HTML: web stranica sa potrebnim funkcijama povezanim sa Python fajlom (tabele, dodavanje hotela, filteri za hotele, itd.)
3. korak - CSS: u dogovoru sa ostalim članovima tima, odredimo astetiku i povežemo sa HTML fajlom

Postupak primene:
Nakon preuzimanja fajlova sa Github-a, preuzmu se Flask, my-sql-connector, i ostale aplikacije zadate u fajlu "requirements.txt",
potom se povežemo na MySQL server i ručno importujemo bazu podataka ("Create database" -> ispišemo ime baze -> dugme "Create" -> "Import" -> izaberemo preuzet SQL fajl -> dugme "Import").
Kad to obavimo, Python aplikacija "app.py" se pokreće preko debugger-a (Python Debugger: Flask)
