from training.model import *
from training.extensions import ma


#Todo: for all Schemas, considering adding HyperLinkRelated for Forgein Keys
class AthleteSchema(ma.ModelSchema):
    class Meta:
        model = Athlete

    personalbest = ma.List(ma.HyperlinkRelated("athlete./api/personalbest"))
    trainingweek = ma.List(ma.HyperlinkRelated("training./api/trainingweek"))


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

    traininglap = ma.List(ma.HyperlinkRelated("training./api/traininglap"))


class TempoSchema(ma.ModelSchema):
    class Meta:
        model = Tempo


class TrainingLapSchema(ma.ModelSchema):
    class Meta:
        include_fk = True
        model = TrainingLap


class TrainingWeekSchema(ma.ModelSchema):
    class Meta:
        include_fk = True
        model = TrainingWeek

    schedules = ma.List(ma.HyperlinkRelated("training./api/trainingweekschedule"))


class TrainingWeekScheduleSchema(ma.ModelSchema):
    class Meta:
        include_fk = True
        model = TrainingWeekSchedule


class VdotSchema(ma.ModelSchema):
    class Meta:
        model = Vdot


class VdotTempoSchema(ma.ModelSchema):
    class Meta:
        include_fk = True
        model = VdotTempo
