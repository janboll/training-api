from training import db

"""
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
"""


class TrainingType(db.Model):
    __tablename__ = "training_type"
    id = db.Column(db.Integer, primary_key=True)
    # "alternating", "increasing", "steady"
    type_name = db.Column(db.String, nullable=False)


class Tempo(db.Model):
    __tablename__ = "tempo"
    id = db.Column(db.Integer, primary_key=True)
    lower_percentage_hr = db.Column(db.Float, nullable=False)
    upper_percentage_hr = db.Column(db.Float, nullable=False)
    lower_percentage_max_vdot = db.Column(db.Float, nullable=False)
    upper_percentage_max_vdot = db.Column(db.Float, nullable=False)
    lower_seconds_per_km = db.Column(db.Integer, nullable=False)
    upper_seconds_per_km = db.Column(db.Integer, nullable=False)
    name = db.Column(db.String, nullable=False)


class TrainingLap(db.Model):
    __tablename__ = "training_lap"
    id = db.Column(db.Integer, primary_key=True)
    training_id = db.Column(db.Integer, db.ForeignKey("training.id"), nullable=False)
    lap = db.Column(db.Integer, nullable=False)
    tempo = db.Column(db.Integer, db.ForeignKey("tempo.id"), nullable=False)
    distance_in_meter = db.Column(db.Integer, nullable=True)
    time_in_seconds = db.Column(db.Integer, nullable=True)
    training = db.relationship("Training", backref="traininglap")


class Training(db.Model):
    """
        Intensity of training can be derived from the VDOT values of the tempo.
            sum(tempo.vdot_percent)
    """

    __tablename__ = "training"
    id = db.Column(db.Integer, primary_key=True)
    training_type_id = db.Column(
        db.Integer, db.ForeignKey("training_type.id"), nullable=False
    )


class Athlete(db.Model):
    __tablename__ = "athlete"
    id = db.Column(db.Integer, primary_key=True)
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.String, nullable=False)
    weight = db.Column(db.Float, nullable=False)


class PersonalBest(db.Model):
    __tablename__ = "personal_best"
    id = db.Column(db.Integer, primary_key=True)
    distance_in_meter = db.Column(db.Integer, nullable=False)
    time_in_seconds = db.Column(db.Integer, nullable=False)
    athlete_id = db.Column(db.Integer, db.ForeignKey("athlete.id"), nullable=False)
    athlete = db.relationship("Athlete", backref="personalbest")
