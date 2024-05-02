import requests

def search_recipes_api(title):
    """Searches for recipes via an external API using GET method."""
    api_url = f'https://api.spoonacular.com/recipes/complexSearch?query={title}&apiKey=2c9a826eab7a408f9575ef4d3e9fe63a&addRecipeInformation=true&instructionsRequired=true'
    headers = {'Content-Type': 'application/json'}
    response = requests.get(api_url, headers=headers)
    if response.status_code == 200:
        print("API Success Response:", response.json())  # Log successful API response
        return response.json()
    else:
        print("API Error Response:", response.status_code, response.text)  # Log error response
        return None

def create_recipe_api(title, instructions, rating, comments):
    """Creates a recipe via an external API using POST method."""
    api_url = 'https://api.spoonacular.com/recipes/complexSearch'  # Ensure this is the correct endpoint for creation
    api_key = '2c9a826eab7a408f9575ef4d3e9fe63a'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {api_key}'
    }
    data = {
        'title': title,
        'instructions': instructions,
        'rating': rating,
        'comments': comments  # Ensure your API supports 'comments' if you're including it
    }
    response = requests.post(api_url, json=data, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        return None
