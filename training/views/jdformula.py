from training.schema import VdotSchema
from training.model.Model import Vdot
from training.views.generic import ApiGeneric, register_api
from training.extensions import db

from flask import Blueprint, request


bp_jdformula = Blueprint("jdformula", __name__)


class ApiVdot(ApiGeneric):
    def _vdot_from_time_and_distance(self, distance_in_meter=None, time_in_seconds=None):
        return (
            self.model.query.filter(
                self.model.distance_in_meter == distance_in_meter,
                self.model.time_in_seconds >= time_in_seconds,
            )
            .order_by(db.desc(self.model.vdot))
            .first()
        )

    def __init__(self):
        super().__init__(
            VdotSchema,
            Vdot,
            query_mappings=[
                {
                    "params": ["distance_in_meter", "time_in_seconds"],
                    "query_func": self._vdot_from_time_and_distance,
                }
            ],
        )


register_api(bp_jdformula, ApiVdot, "/api/vdot")
