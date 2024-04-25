from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/submit_recipe', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        recipe_title = request.form.get('RecipeTitle')
        instructions = request.form.get('instructions')
        reviews = request.form.get('reviews')
        return redirect(url_for('index'))

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
    
    # picture api