from flask import Flask
from training.extensions import db, ma


def create_app():

    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:////tmp/test.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
    db.init_app(app)
    ma.init_app(app)

    from training.views.athlete import bp_athlete
    from training.views.training import bp_training

    app.register_blueprint(bp_athlete)
    app.register_blueprint(bp_training)

    with app.app_context():
        db.create_all()

    return app
