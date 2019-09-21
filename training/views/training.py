from training.schema import (
    TrainingSchema,
    TrainingLapSchema,
    TrainingTypeSchema,
    TempoSchema,
)
from training.model.Model import Training, TrainingLap, TrainingType, Tempo
from training.views.generic import ApiGeneric, register_api

from flask import Blueprint

bp_training = Blueprint("training", __name__)


class ApiTraining(ApiGeneric):
    def __init__(self):
        super().__init__(TrainingSchema, Training)


class ApiTrainingLap(ApiGeneric):
    def __init__(self):
        super().__init__(TrainingLapSchema, TrainingLap)


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
