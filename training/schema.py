from training.model import *
from training.extensions import ma


class AthleteSchema(ma.ModelSchema):
    class Meta:
        model = Athlete

    personalbest = ma.List(ma.HyperlinkRelated("athlete.specific_personalbest"))


class PersonalBestSchema(ma.ModelSchema):
    class Meta:
        include_fk = True
        model = PersonalBest


class TrainingTypeSchema(ma.ModelSchema):
    class Meta:
        model = TrainingType


class TrainingSchema(ma.ModelSchema):
    class Meta:
        include_fk = True
        model = Training

    traininglap = ma.List(ma.HyperlinkRelated("training.specific_traininglap"))


class TempoSchema(ma.ModelSchema):
    class Meta:
        model = Tempo


class TrainingLapSchema(ma.ModelSchema):
    class Meta:
        include_fk = True
        model = TrainingLap
