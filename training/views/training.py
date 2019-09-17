from training.extensions import db, ma
from training.schema import AthleteSchema
from training.model.Model import Training

from flask import Blueprint, request
from flask_marshmallow import exceptions

bp_training = Blueprint("training", __name__)


@bp_training.route("/api/training", methods=["GET", "POST"])
def training():
    pass

"""
@bp_training.route("/api/training/<id:int>")
def training_by_id():
    db.create_all()
    all_athletes = Athlete.query.all()
    return AthleteSchema().jsonify(all_athletes)
"""

@bp_training.route("/api/traininglap/")
def traininglap():
    pass
