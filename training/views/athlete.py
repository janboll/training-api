from training.extensions import db
from training.schema import AthleteSchema, PersonalBestSchema
from training.model.Model import Athlete, PersonalBest
from .response import _error_not_found, _error_validation, _notif_item_created

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
            return _error_validation(e)
        db.session.add(new_athlete)
        db.session.commit()
        return _notif_item_created("Athlete")
    elif request.method == "GET":
        all_athletes = Athlete.query.all()
        return AthleteSchema(many=True).jsonify(all_athletes)


@bp_athlete.route("/api/athlete/<int:id>", methods=["GET"])
def specific_athlete(id):
        athlete = Athlete.query.get(id)
        if athlete:
            return AthleteSchema().jsonify(athlete)
        return _error_not_found("Athlete", id)


@bp_athlete.route("/api/personalbest", methods=["GET", "POST"])
def personalbest():
    if request.method == "POST":
        json_data = request.get_json()
        try:
            new_personal_best = PersonalBestSchema().load(json_data)
        except exceptions.ValidationError as e:
            return _error_validation(e)
        db.session.add(new_personal_best)
        db.session.commit()
        return _notif_item_created("PersonalBest")
    elif request.method == "GET":
        all_personal_bests = PersonalBest.query.all()
        return PersonalBestSchema(many=True).jsonify(all_personal_bests)


@bp_athlete.route("/api/personalbest/<int:id>", methods=["GET"])
def specific_personalbest(id):
    personal_best = PersonalBest.query.get(id)
    if personal_best:
        return PersonalBestSchema().jsonify(personal_best)
    return _error_not_found("PersonalBest", id)
