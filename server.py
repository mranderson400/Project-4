from flask_app import app
from flask_app.controllers import users_controller, main_controller

if __name__ == "__main__":
    app.run( debug=True, port=5011) #this runs the app initialized in our init 

