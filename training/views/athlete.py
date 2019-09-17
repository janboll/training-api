from training.schema import AthleteSchema, PersonalBestSchema
from training.model.Model import Athlete, PersonalBest
from .response import _error_not_found
from .generic import _entity_default_endpoint, _entity_specific_endpoint

from flask import Blueprint, request

bp_athlete = Blueprint("athlete", __name__)


@bp_athlete.route("/api/athlete", methods=["GET", "POST"])
def athlete():
    return _entity_default_endpoint(Athlete, AthleteSchema, request)


@bp_athlete.route("/api/athlete/<int:id>", methods=["GET"])
def specific_athlete(id):
    return _entity_specific_endpoint(Athlete, AthleteSchema, id)


@bp_athlete.route("/api/personalbest", methods=["GET", "POST"])
def personalbest():
    return _entity_default_endpoint(PersonalBest, PersonalBestSchema, request)


@bp_athlete.route("/api/personalbest/<int:id>", methods=["GET"])
def specific_personalbest(id):
    return _entity_specific_endpoint(PersonalBest, PersonalBestSchema, id)
