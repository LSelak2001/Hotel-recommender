from flask import Blueprint, render_template, request, redirect, url_for, flash, abort
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps
from routes.ekstenzije import db
from routes.modeli import User

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
    user = None
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        remember = 'remember' in request.form
        user = User.query.filter_by(email=email).first()
        if user and check_password_hash(pwhash=user.password, password=password):
            login_user(user, remember=remember)
            return redirect(url_for('dashboard'))
        flash('Invalid email or password')
    return render_template('login.html')

@korisnik_bp.route('/register', methods=['GET', 'POST'])
def register():
    user = None
    if request.method == 'POST':
        username: str = request.form['username']
        email: str = request.form['email']
        password: str = generate_password_hash(request.form['password'])
        user = User(username,
                    email,
                    check_password_hash(pwhash=user.password, password=password))
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('register.html')

@korisnik_bp.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html')

@korisnik_bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))