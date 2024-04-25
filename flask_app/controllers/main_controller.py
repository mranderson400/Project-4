from flask_app import app
from flask import render_template,redirect,request,flash,session



@app.route('/')
def index():
    
    return render_template("welcome.html")

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


