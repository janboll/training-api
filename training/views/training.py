from training.schema import (
    TrainingSchema,
    TrainingLapSchema,
    TrainingTypeSchema,
    TempoSchema,
)
from training.model.Model import Training, TrainingLap, TrainingType, Tempo
from training.views.generic import ApiGeneric, register_api

from flask import Blueprint, request

bp_training = Blueprint("training", __name__)


class ApiTraining(ApiGeneric):
    def __init__(self):
        super().__init__(TrainingSchema, Training)


class ApiTrainingLap(ApiGeneric):
    def _by_training_id(self, training_id=None):
        return self.model.query.filter(self.model.training_id == training_id).all()

    def __init__(self):
        super().__init__(
            TrainingLapSchema,
            TrainingLap,
            query_mappings=[
                {"params": ["training_id"], "query_func": self._by_training_id}
            ],
        )


class ApiTrainingType(ApiGeneric):
    def __init__(self):
        super().__init__(TrainingTypeSchema, TrainingType)


class ApiTempo(ApiGeneric):
    def __init__(self):
        super().__init__(TempoSchema, Tempo)


register_api(bp_training, ApiTraining, "/api/training")
register_api(bp_training, ApiTrainingLap, "/api/traininglap")
register_api(bp_training, ApiTrainingType, "/api/trainingtype")
register_api(bp_training, ApiTempo, "/api/tempo")
