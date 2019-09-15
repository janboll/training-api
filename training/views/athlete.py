from training.extensions import db
from training.schema import AthleteSchema
from training.model.Model import Athlete, PersonalBest

from flask import Blueprint

bp_athlete = Blueprint("athlete", __name__)


@bp_athlete.route("/api/athlete/")
def athlete():
    db.create_all()
    all_athletes = Athlete.query.all()
    return AthleteSchema().jsonify(all_athletes)


@bp_athlete.route("/api/personalbest/")
def personalbest():
    pass
