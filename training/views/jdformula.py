from training.schema import VdotSchema
from training.model.Model import Vdot
from training.views.generic import ApiGeneric, register_api

from flask import Blueprint, request

bp_jdformula = Blueprint("jdformula", __name__)


class ApiVdot(ApiGeneric):
    def _time_in_seconds_query(self, time_in_seconds=None):
        return self.model.query.filter(self.model.time_in_seconds == time_in_seconds).all()

    def __init__(self):
        super().__init__(
            VdotSchema,
            Vdot,
            query_mappings=[
                {
                    "params": ["time_in_seconds"],
                    "query_func": self._time_in_seconds_query,
                }
            ],
        )


register_api(bp_jdformula, ApiVdot, "/api/vdot")
