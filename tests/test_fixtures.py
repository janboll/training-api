from training import app, create_app, default_settings
from training.extensions import db
from training.model.Model import Athlete, PersonalBest

import json
import os
import pytest
import tempfile


def client_data_to_dict(data, encoding="utf-8"):
    return json.loads(data.decode(encoding))


@pytest.fixture
def client():
    fd, db_file = tempfile.mkstemp()
    default_settings.SQLALCHEMY_DATABASE_URI = "sqlite:///{}".format(db_file)

    with app.test_client() as client:
        with app.app_context():
            create_app()
        yield client

    os.close(fd)
    os.unlink(db_file)


@pytest.fixture
def add_athlete_with_pb():
    with app.app_context():
        athlete = Athlete(age=32, gender="w", weight="60")
        pb = PersonalBest(distance_in_meter=1000, time_in_seconds=50, athlete_id=1)
        db.session.add(athlete)
        db.session.add(pb)
        db.session.commit()
