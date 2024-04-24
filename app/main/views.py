from flask import Blueprint, render_template, request
import requests


from app.models import EditableHTML

main = Blueprint('main', __name__)

API_URL = 'https://api.spoonacular.com/recipes/complexSearch'
API_KEY = '2c9a826eab7a408f9575ef4d3e9fe63a'

@main.route('/')
@main.route('/index')
def index():
    # Make an HTTP GET request to the Spoonacular API
    url = f'{API_URL}?query=pasta&apiKey={API_KEY}&addRecipeInformation=true&instructionsRequired=true'
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # this parses the JSON response
        data = response.json()
        recipes = data['results']  # This basically extracts the 'array' of recipe objects

        # Pass the recipe data to the template for rendering
        return render_template('main/index.html', recipes=recipes)
    else:
        # Handle error cases, such as API request failure
        error_message = 'Failed to fetch recipes. Please try again later.'
        return render_template('errors/403.html', error_message=error_message)

@main.route('/search_recipes', methods=['GET'])
def search_recipes():
    # Get the search query from the request
    query = request.args.get('query')

    # Make a request to the Spoonacular API to search for recipes
    url = f'{API_URL}?query={query}&apiKey={API_KEY}&addRecipeInformation=true&instructionsRequired=true'
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        recipes = data.get('results', [])
        return render_template('main/index.html', recipes=recipes)
    else:
        error_message = f"Failed to fetch recipes. Status code: {response.status_code}"
        return render_template('error.html', error_message=error_message)




@main.route('/about')
def about():
    return render_template('main/about.html')

