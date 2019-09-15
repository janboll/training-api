from training.extensions import db
from training.schema import AthleteSchema
from training.model.Model import Athlete, PersonalBest

from flask import Blueprint

bp_training = Blueprint("training", __name__)


@bp_training.route("/api/training/")
def training():
    db.create_all()
    all_athletes = Athlete.query.all()
    return AthleteSchema().jsonify(all_athletes)


@bp_training.route("/api/traininglap/")
def traininglap():
    pass
