from flask import Flask
from training.extensions import db, ma

app = Flask(__name__)


def create_app():

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:////tmp/test.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
    db.init_app(app)
    ma.init_app(app)

    from training.views.athlete import bp_athlete
    from training.views.training import bp_training
    from training.views.jdformula import bp_jdformula

    app.register_blueprint(bp_athlete)
    app.register_blueprint(bp_training)
    app.register_blueprint(bp_jdformula)

    from .error_handlers import error_not_found
    from .error_handlers import error_validation

    with app.app_context():
        db.create_all()

    return app
