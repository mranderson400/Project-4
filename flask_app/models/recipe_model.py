from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_app import db  

class Recipe(db.Model):
    __tablename__ = 'recipes'  

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    instructions = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    review = db.Column(db.Integer, nullable=True)  

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)  
    user = db.relationship('User', backref='recipes')  

    def __repr__(self):
        return f'<Recipe {self.title}>'
