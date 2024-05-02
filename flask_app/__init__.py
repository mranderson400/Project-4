from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import flask_sqlalchemy
import sqlalchemy

# Create the Flask application
app = Flask(__name__)

# Configuration settings
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'  # Adjust as necessary
app.config['SECRET_KEY'] = 'is it really a secret tho'  # Make sure this is set properly

# Initialize SQLAlchemy and Migrate
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Import and register the blueprints after db to avoid circular imports


# Display SQLAlchemy versions for debugging purposes
print("SQLAlchemy version:", sqlalchemy.__version__)
print("Flask-SQLAlchemy version:", flask_sqlalchemy.__version__)

# Additional configurations or imports can go here
