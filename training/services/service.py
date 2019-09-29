from training.schema import PersonalBestSchema, AthleteSchema
from training.model import Athlete, Vdot
from training.extensions import db


def update_athlete_vdot_from_pb(pb: PersonalBestSchema):
    vdot = Vdot.query.filter(
            Vdot.distance_in_meter == pb.distance_in_meter,
            Vdot.time_in_seconds >= pb.time_in_seconds,
            ).order_by(db.desc(Vdot.vdot)).first()

    # TODO: check if vdot changed
    athlete = Athlete.query.get(pb.athlete_id)
    if athlete.vdot_value is None or athlete.vdot_value < vdot.vdot:
        athlete.vdot_value = vdot.vdot
        db.session.add(athlete)
        db.session.commit()
