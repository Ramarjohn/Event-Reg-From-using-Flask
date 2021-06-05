from . import db


class Userevent(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100))
    phone =db.Column(db.Integer)
    # password = db.Column(db.String(100))
    name = db.Column(db.String(100))
    gender=db.Column(db.String(100))
