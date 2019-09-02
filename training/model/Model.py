"""from training import db


class Training(db.Model):
    id = db.Column(db.Integer, primary_key=True)


class Session(db.Model):
    id = db.Column(db.Integer, primary_key=True)


class Schedule(db.Model):
    id = db.Column(db.Integer, primary_key=True)


class Week(db.Model):
    id = db.Column(db.Integer, primary_key=True)
"""
from training import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255))

