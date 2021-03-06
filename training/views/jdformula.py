from training.schema import VdotSchema, VdotTempoSchema
from training.model.Model import Vdot, VdotTempo
from training.views.generic import ApiGeneric, register_api
from training.extensions import db

from flask import Blueprint, request


bp_jdformula = Blueprint("jdformula", __name__)


class ApiVdot(ApiGeneric):
    def _vdot_from_time_and_distance(
        self, distance_in_meter=None, time_in_seconds=None
    ):
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


class ApiVdotTempo(ApiGeneric):
    def _get_tempo_for_vdot(self, vdot=None, tempo=None):
        return self.model.query.filter(
            self.model.vdot == vdot, self.model.tempo == tempo
        ).all()

    def __init__(self):
        super().__init__(
            VdotTempoSchema,
            VdotTempo,
            query_mappings=[
                {"params": ["vdot", "tempo"], "query_func": self._get_tempo_for_vdot}
            ],
        )


register_api(bp_jdformula, ApiVdot, "/api/vdot")
register_api(bp_jdformula, ApiVdotTempo, "/api/vdot_tempo")
