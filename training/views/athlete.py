from training.schema import AthleteSchema, PersonalBestSchema
from training.model.Model import Athlete, PersonalBest
from training.views.generic import ApiGeneric, register_api

from training.services.service import update_athlete_vdot_from_pb

from flask import Blueprint, request


class ApiPersonalBest(ApiGeneric):
    def _get_pb_by_athlete_id(self, athlete_id=None):
        return self.model.query.filter(self.model.athlete_id == athlete_id).all()

    def __init__(self):
        super().__init__(
            PersonalBestSchema,
            PersonalBest,
            query_mappings=[
                {"params": ["athlete_id"], "query_func": self._get_pb_by_athlete_id}
            ],
        )

    def post(self):
        pb = self._get_item_from_request()
        post_result = self._post_single_item(pb)

        update_athlete_vdot_from_pb(pb)

        return post_result


class ApiAthlete(ApiGeneric):
    def __init__(self):
        super().__init__(AthleteSchema, Athlete)


bp_athlete = Blueprint("athlete", __name__)

register_api(bp_athlete, ApiAthlete, "/api/athlete")
register_api(bp_athlete, ApiPersonalBest, "/api/personalbest")
