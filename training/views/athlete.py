from training.extensions import db
from training.schema import AthleteSchema
from training.model.Model import Athlete, PersonalBest
from . import _validation_error_response, _not_found_error

from flask import Blueprint, request
from flask_marshmallow import exceptions

bp_athlete = Blueprint("athlete", __name__)


@bp_athlete.route("/api/athlete", methods=["GET", "POST"])
def athlete():
    if request.method == "POST":
        json_data = request.get_json()
        try:
            new_athlete = AthleteSchema().load(json_data)
        except exceptions.ValidationError as e:
            return _validation_error_response(e)
        db.session.add(new_athlete)
        db.session.commit()
        return {"notification": "athlete created"}, 201
    elif request.method == "GET":
        all_athletes = Athlete.query.all()
        print(all_athletes)
        return AthleteSchema(many=True).jsonify(all_athletes)


@bp_athlete.route("/api/athlete/<int:id>", methods=["GET"])
def specific_athlete(id):
        athlete = Athlete.query.get(id)
        if athlete:
            return AthleteSchema().jsonify(athlete)
        return _not_found_error("Athlete", id)


@bp_athlete.route("/api/personalbest/")
def personalbest():
    pass
