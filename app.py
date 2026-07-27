from flask import Flask, render_template, redirect, url_for, request, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from routes.hoteli import hoteli_bp
from routes.smestaj import smestaj_bp
from datetime import timedelta
from functools import wraps
from flask import abort

app = Flask(__name__) # rutina za kreiranje aplikacije
app.config['SECRET_KEY'] = 'your-secret-key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['REMEMBER_COOKIE_DURATION'] = timedelta(days=30)

db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

app.register_blueprint(hoteli_bp)
app.register_blueprint(smestaj_bp)

def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user.is_authenticated or not current_user.is_admin:
            abort(403)  # Forbidden
        return f(*args, **kwargs)
    return decorated_function

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/admin')
@login_required
@admin_required
def admin_dashboard():
    users = User.query.all()  # Fetch all users to display
    return render_template('admin.html', users=users)

@app.route('/login', methods=['GET', 'POST'])
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

@app.route('/register', methods=['GET', 'POST'])
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

@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

if __name__ == "__main__":  # program startuje app.py
    with app.app_context():
        db.create_all()
    app.run(debug = True)  # Promeniti na kraju projekta na False, da se ne bi prikazivali detalji o greškama korisnicima.