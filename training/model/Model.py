from training import db

import enum


class Gender(enum.Enum):
    m = "male"
    f = "female"


class Training(db.Model):
    """
        Intensity of training can be derived from the VDOT values of the tempo.
            sum(tempo.vdot_percent)
    """
    id = db.Column(db.Integer, primary_key=True)
    type = ["alternating", "increasing", "steady"] # Alternate between tempos, increase or run the same
    tempo = ["tempo specification"] # depending on VDOT, freely configurable
    repetitions = ["if alternating, number of reps"]


class Session(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    training = [Training] # reference to training
    data = [] # Data retrieved from Garmin


class Schedule(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    weeknumner = []
    start_date = []
    end_data = []
    training = [] # list of trainings, None means off


class TrainingPlan(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    trainings = []


class Athlete(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.Enum(Gender), nullable=False)
    weight = db.Column(db.Float, nullable=False)
    #personal_bests = db.relationship("PersonalBest", back_populates="athlete")


class PersonalBest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    distance_in_meter = db.Column(db.Integer, nullable=False)
    time_in_seconds = db.Column(db.Integer, nullable=False)
    athlete_id = db.Column(db.Integer, db.Foreign_Key("Athlete.id"), nullable=False)

