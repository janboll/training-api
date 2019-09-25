from training.schema import AthleteSchema, PersonalBestSchema
from training.model.Model import Athlete, PersonalBest
from training.views.generic import ApiGeneric, register_api

from flask import Blueprint


class ApiPersonalBest(ApiGeneric):
    def __init__(self):
        super().__init__(
            PersonalBestSchema, PersonalBest, allowed_query_params=["athlete_id"]
        )


class ApiAthlete(ApiGeneric):
    def __init__(self):
        super().__init__(AthleteSchema, Athlete)


bp_athlete = Blueprint("athlete", __name__)

register_api(bp_athlete, ApiAthlete, "/api/athlete")
register_api(bp_athlete, ApiPersonalBest, "/api/personalbest")
