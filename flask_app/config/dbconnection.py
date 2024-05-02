
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connectToSQLite(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///recipes.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
