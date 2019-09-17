from training.schema import TrainingSchema, TrainingLapSchema, TrainingTypeSchema, TempoSchema
from training.model.Model import Training, TrainingLap, TrainingType, Tempo
from .generic import _entity_default_endpoint, _entity_specific_endpoint

from flask import Blueprint, request

bp_training = Blueprint("training", __name__)


@bp_training.route("/api/tempo", methods=["GET", "POST"])
def tempo():
    return _entity_default_endpoint(Tempo, TempoSchema, request)


@bp_training.route("/api/tempo/<int:id>", methods=["GET"])
def specific_tempo(id):
    return _entity_specific_endpoint(Tempo, TempoSchema, id)


@bp_training.route("/api/training", methods=["GET", "POST"])
def training():
    return _entity_default_endpoint(Training, TrainingSchema, request)


@bp_training.route("/api/training/<int:id>", methods=["GET"])
def specific_training(id):
    return _entity_specific_endpoint(Training, TrainingSchema, id)


@bp_training.route("/api/traininglap", methods=["GET", "POST"])
def traininglap():
    return _entity_default_endpoint(TrainingLap, TrainingLapSchema, request)


@bp_training.route("/api/traininglap/<int:id>", methods=["GET"])
def specific_traininglap(id):
    return _entity_specific_endpoint(TrainingLap, TrainingLapSchema, id)


@bp_training.route("/api/trainingtype", methods=["GET", "POST"])
def trainingtype():
    return _entity_default_endpoint(TrainingType, TrainingTypeSchema, request)


@bp_training.route("/api/trainingtype/<int:id>", methods=["GET"])
def specific_trainingtype(id):
    return _entity_specific_endpoint(TrainingType, TrainingTypeSchema, id)

