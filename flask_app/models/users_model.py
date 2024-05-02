from flask_app import db 
from flask import flash
import re
from datetime import datetime

class User(db.Model):
    __tablename__ = 'user'  
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(150), nullable=False)
    last_name = db.Column(db.String(150), nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    @staticmethod
    def validate(form_data):
        is_valid = True
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(form_data['email']):
            flash("Invalid email address!", 'register')
            is_valid = False
        if len(form_data['first_name']) < 2 or len(form_data['last_name']) < 2:
            flash("First and last name must be at least 2 characters long", 'register')
            is_valid = False
        if len(form_data['password']) < 8:
            flash("Password must be at least 8 characters long", 'register')
            is_valid = False
        if 'confirm_password' in form_data and form_data['password'] != form_data['confirm_password']:
            flash("Passwords do not match", 'register')
            is_valid = False
        return is_valid



    @classmethod
    def create(cls, data):
        user = cls(
            first_name=data['first_name'],
            last_name=data['last_name'],
            email=data['email'],
            password=data['password']
        )
        try:
            db.session.add(user)
            db.session.commit()
            return user.id
        except Exception as e:
            flash("Error registering user: " + str(e), 'register')
            db.session.rollback()
            return None
    @classmethod
    def get_by_email(cls, data):
        email = data.get('email')
        if email:
            return cls.query.filter_by(email=email).first()
        return None
