from datetime import datetime

from src.extensions import db

class Link(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    short_code = db.Column(db.String(8), index = True, unique = True)
    short_link = db.Column(db.String(32), index = True, unique = True)
    original_link = db.Column(db.String(4096), index = True, unique = False)
    uses = db.Column(db.Integer, index = True, unique = False)
    created_at = db.Column(db.DateTime(), index = True, unique = False, default = datetime.now())
    creator_id = db.Column(db.Integer, db.ForeignKey('user.id'))
