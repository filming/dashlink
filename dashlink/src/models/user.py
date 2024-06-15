from flask_login import UserMixin

from datetime import datetime

from src.extensions import db

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(16), index = True, unique = True)
    email = db.Column(db.String(64), index = True, unique = True)
    password = db.Column(db.String(64), index = False, unique = False)
    creation_date = db.Column(db.DateTime(), index = True, default = datetime.now())
    