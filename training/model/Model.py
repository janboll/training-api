from training import db


class Training(db.Model):
    id = db.Column(db.Integer, primary_key=True)


class Session(db.Model):
    id = db.Column(db.Integer, primary_key=True)


class Schedule(db.Model):
    id = db.Column(db.Integer, primary_key=True)


class Week(db.Model):
    id = db.Column(db.Integer, primary_key=True)

