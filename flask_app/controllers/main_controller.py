# from flask_sqlalchemy import SQLAlchemy
# from flask_app import app
# from flask import render_template,redirect,request,flash,session, url_for
# from flask_app.models.users_model import User
# from flask_app.models.recipe_model import Recipe  
# # db = SQLAlchemy(app)


# from flask_sqlalchemy import SQLAlchemy
# from flask_app import app
# from flask import render_template, redirect, request, flash, session, url_for
# from flask_app.models.users_model import User
# from flask_app.models.recipe_model import Recipe

# @app.route('/creates')
# def index():
#     # Assuming 'welcome.html' is your main recipe display page and you want to display all recipes there
#     recipes = Recipe.query.all()
#     return render_template('welcome.html', recipes=recipes)

# @app.route('/add_recipe', methods=['POST'])
# def add_recipe():
#     user_id = session.get('user_id')  # Get user_id from session
#     if not user_id:
#         flash('You must be logged in to add a recipe', 'error')
#         return redirect(url_for('index'))  # Assuming 'login' is the endpoint for login page

#     title = request.form['title']
#     instructions = request.form['instructions']
#     review = request.form.get('review')

#     new_recipe = Recipe(title=title, instructions=instructions, review=review, user_id=user_id)
#     db.session.add(new_recipe)
#     db.session.commit()

#     flash('Recipe added successfully!', 'success')
#     return redirect(url_for('welcome'))  # Ensure 'welcome' is the correct endpoint






# # @app.route('/')
# # def index():
# #     if 'likes' not in session:
# #         session['likes'] = 0
# #     return render_template("welcome.html", likes=session['likes'])

# # @app.route('/toggle_like', methods=['POST'])
# # def toggle_like():
# #     liked = request.form.get('liked', 'false') == 'true'
# #     if liked:
# #         session['likes'] += 1
# #     else:
# #         session['likes'] = max(0, session['likes'] - 1)
# #     return redirect(url_for('/'))


