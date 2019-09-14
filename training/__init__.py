from flask import Flask
from training.extensions import db, ma


def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:////tmp/test.db"
    db.init_app(app)
    ma.init_app(app)

    from training.views import blue_print

    app.register_blueprint(blue_print)

    return app
