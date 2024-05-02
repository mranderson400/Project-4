from flask_app import app
from flask import render_template, redirect, request, flash, session,url_for
from flask_app.models.users_model import User
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)






@app.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']
    
    user = User.query.filter_by(email=email).first()
    if user and bcrypt.check_password_hash(user.password, password):
        session['user_id'] = user.id
        session['first_name'] = user.first_name
        return redirect(url_for('welcome'))  # Assuming 'portal' is the endpoint for the portal page
    else:
        flash('Invalid credentials', 'error')
        return redirect(url_for('register'))  # Assuming 'register' is the endpoint for the index page

@app.route('/', methods=['GET', 'POST'], endpoint='register')
def register():
    if request.method == 'POST':
        if not User.validate(request.form):
            return redirect(url_for('register'))
        hashed_pass = bcrypt.generate_password_hash(request.form['password']).decode('utf-8')
        data = {
            'first_name': request.form['first_name'],
            'last_name': request.form['last_name'],
            'email': request.form['email'],
            'password': hashed_pass
        }
        logged_user_id = User.create(data)
        if not logged_user_id:
            return redirect(url_for('register'))
        session['user_id'] = logged_user_id
        session['first_name'] = request.form['first_name']
        return redirect(url_for('welcome'))  # Adjust if there is a specific function for '/welcome'
    else:
        return render_template('index.html')

@app.route('/users/login', methods=['GET', 'POST'])
def log_user():
    if request.method == 'POST':
        data = {'email': request.form['email']}
        user_in_db = User.get_by_email(data)
        if not user_in_db or not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
            flash("Invalid credentials", 'log')
            return redirect(url_for('register'))
        session['user_id'] = user_in_db.id
        session['first_name'] = user_in_db.first_name
        return redirect(url_for('welcome'))
    return render_template('index.html')

@app.route('/welcome')
def welcome():
    # Ensure user is logged in or redirect
    if 'user_id' not in session:
        return redirect(url_for('register'))
    return render_template('welcome.html')

@app.route('/users/logout')
def logout():
    session.clear()
    return redirect(url_for('register'))
