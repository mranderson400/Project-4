import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_app import app
from flask import render_template,redirect,request,flash,session, url_for
from flask_app.models.users_model import User
from flask_app.models.api_services import search_recipes_api, create_recipe_api

from flask_app.models.recipe_model import Recipe  
from datetime import datetime
from flask_app import db 

@app.route('/create')
def create_link():
    # Assuming 'welcome.html' is your main recipe display page and you want to display all recipes there
    return render_template('create.html')

@app.route('/add_recipe', methods=['GET','POST'])
def add_recipe():
    user_id = session.get('user_id')  # Ensure user is logged in
    if not user_id:
        flash('You must be logged in to add a recipe', 'error')
        return redirect(url_for('login'))

    title = request.form.get('title')
    instructions = request.form.get('instructions')
    review = request.form.get('review')
    date_str = request.form.get('date')

    # Convert date from string to datetime object
    try:
        date = datetime.strptime(date_str, '%Y-%m-%d') if date_str else datetime.now()
    except ValueError:
        flash('Invalid date format. Please enter a valid date.', 'error')
        return redirect(url_for('creates'))  # Assuming 'creates' is the endpoint for the recipe creation form

    new_recipe = Recipe(title=title, instructions=instructions, review=review, date=date, user_id=user_id)
    db.session.add(new_recipe)
    try:
        db.session.commit()
        flash('Recipe added successfully!', 'success')
    except Exception as e:
        db.session.rollback()
        flash('Error adding recipe: {}'.format(str(e)), 'error')

    return redirect(url_for('welcome')) 

# API Search


@app.route('/search_recipes', methods=['POST'])
def search_recipes():
    title = request.form['recipe_title']
    recipe_data = search_recipes_api(title)
    if recipe_data:
        print("API Response:", recipe_data)  # Log the API response data
        return render_template('welcome.html', recipe_data=recipe_data)
    else:
        print("Failed to fetch recipes")  # Log an error message
        return render_template('welcome.html', error="Failed to fetch recipes")

@app.route('/create_recipe', methods=['POST'])
def create_recipe():
    title = request.form['title']
    instructions = request.form['instructions']
    rating = request.form['rating']
    comments = request.form.get('comments', '')
    response = create_recipe_api(title, instructions, rating, comments)
    if response:
        return render_template('welcome.html', success="Recipe created successfully")
    else:
        return render_template('welcome.html', error="Failed to create recipe")















# @app.route('/')
# def index():
#     if 'likes' not in session:
#         session['likes'] = 0
#     return render_template("welcome.html", likes=session['likes'])

# @app.route('/toggle_like', methods=['POST'])
# def toggle_like():
#     liked = request.form.get('liked', 'false') == 'true'
#     if liked:
#         session['likes'] += 1
#     else:
#         session['likes'] = max(0, session['likes'] - 1)
#     return redirect(url_for('/'))


