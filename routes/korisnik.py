from flask import Blueprint, render_template, request, redirect, url_for, flash, abort
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps
from routes.ekstenzije import db
from routes.modeli import User
from sqlalchemy.exc import IntegrityError

korisnik_bp = Blueprint("korisnik", __name__)   # kreira Blueprint za korisničke rute, što omogućava modularizaciju aplikacije i organizaciju ruta u odvojene komponente.

def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user.is_authenticated or not current_user.is_admin:
            abort(403)  # Zahtjev je odbijen ako korisnik nije prijavljen ili nije administrator.
        return f(*args, **kwargs)
    return decorated_function

@korisnik_bp.route('/admin')    # Prikaz svih korisnika u bazi podataka, što omogućava administratoru da vidi i upravlja korisnicima.
@login_required
@admin_required
def admin_dashboard():
    users = User.query.all()  
    return render_template('admin.html', users=users)

@korisnik_bp.route('/login', methods=['GET', 'POST'])
def login():
    korisnik = None
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        remember = 'remember' in request.form
        korisnik = User.query.filter_by(email=email).first()
        if korisnik and check_password_hash(pwhash=korisnik.password, password=password):
            login_user(korisnik, remember=remember)
            return redirect(url_for('korisnik.admin_dashboard') if korisnik.is_admin else url_for('korisnik.dashboard'))
        flash('Invalid email or password')
    return render_template('login.html')

@korisnik_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password_hashed = generate_password_hash(request.form['password'])

        if User.query.filter_by(email=email).first():
            flash('Email already registered')
            return render_template('register.html')

        korisnik = User(username=username, email=email, password=password_hashed, role='korisnik')
        db.session.add(korisnik)
        try:
            db.session.commit()
        except IntegrityError:
            db.session.rollback()
            flash('Registration error — please try a different email')
            return render_template('register.html')

        return redirect(url_for('korisnik.login'))
    return render_template('register.html')

@korisnik_bp.route('/dashboard')
@login_required
def dashboard():
    return render_template('admin.html')

@korisnik_bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('korisnik.login'))