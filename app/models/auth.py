from app.extensions import db

from flask_login import UserMixin

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(20) ,nullable=False)
    last_name = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(30), nullable=False,unique=True)
    phone_number = db.Column(db.String(15))
    password = db.Column(db.String(100), nullable=False)