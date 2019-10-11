from training import db


class Vdot(db.Model):
    __tablename__ = "vdot_values"
    id = db.Column(db.Integer, primary_key=True)
    vdot = db.Column(db.Float, nullable=False)
    distance_in_meter = db.Column(db.Integer, nullable=False)
    time_in_seconds = db.Column(db.Integer, nullable=False)


class VdotTempo(db.Model):
    __tablename__ = "vdot_tempo_values"
    id = db.Column(db.Integer, primary_key=True)
    tempo = db.Column(db.Integer, db.ForeignKey("tempo.id"), nullable=False)
    vdot = db.Column(db.Float, nullable=False)
    pace_in_seconds_per_km = db.Column(db.Integer, nullable=False)
    distance_in_meter = db.Column(db.Integer, nullable=True)


class Tempo(db.Model):
    __tablename__ = "tempo"
    id = db.Column(db.Integer, primary_key=True)
    lower_percentage_hr = db.Column(db.Float, nullable=False)
    upper_percentage_hr = db.Column(db.Float, nullable=False)
    lower_percentage_max_vdot = db.Column(db.Float, nullable=False)
    upper_percentage_max_vdot = db.Column(db.Float, nullable=False)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=True)


class TrainingWeek(db.Model):
    __tablename__ = "training_week"
    id = db.Column(db.Integer, primary_key=True)
    start_date = db.Column(db.Date, nullable=False)
    athlete_id = db.Column(db.Integer, db.ForeignKey("athlete.id"), nullable=False)


class TrainingWeekSchedule(db.Model):
    __tablename__ = "training_week_schedule"
    id = db.Column(db.Integer, primary_key=True)
    training_week_id = db.Column(
        db.Integer, db.ForeignKey("training_week.id"), nullable=False
    )
    training_id = db.Column(db.Integer, db.ForeignKey("training.id"), nullable=False)


class TrainingLap(db.Model):
    # TODO: PK should be composite of training_id, lap
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


class TrainingType(db.Model):
    __tablename__ = "training_type"
    id = db.Column(db.Integer, primary_key=True)
    type_name = db.Column(db.String, nullable=False)


class Athlete(db.Model):
    __tablename__ = "athlete"
    id = db.Column(db.Integer, primary_key=True)
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.String, nullable=False)
    weight = db.Column(db.Float, nullable=False)
    vdot_value = db.Column(db.Integer, nullable=True)


class PersonalBest(db.Model):
    __tablename__ = "personal_best"
    id = db.Column(db.Integer, primary_key=True)
    distance_in_meter = db.Column(db.Integer, nullable=False)
    time_in_seconds = db.Column(db.Integer, nullable=False)
    athlete_id = db.Column(db.Integer, db.ForeignKey("athlete.id"), nullable=False)
    athlete = db.relationship("Athlete", backref="personalbest")
