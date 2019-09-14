from training.extensions import db
from training.schema import athletes_schema
from training.model.Model import Athlete, PersonalBest

from flask import Blueprint

blue_print = Blueprint("basic", __name__)


@blue_print.route("/api/athlete/")
def athlete():
    db.create_all()
    all_athletes = Athlete.query.all()
    return athletes_schema.jsonify(all_athletes)


@blue_print.route("/api/personalbest/")
def personalbest():
    pass
