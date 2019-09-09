from flask import Flask
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
ma = Marshmallow()


def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:////tmp/test.db"
    db.init_app(app)
    ma.init_app(app)

    from training.model import Athlete, PersonalBest

    class AthleteSchema(ma.Schema):
        class Meta:
            model = Athlete

    athletes_schema = AthleteSchema(many=True)

    @app.route("/api/athletes/")
    def athletes():
        db.create_all()
        all_athletes = Athlete.query.all( )
        a = athletes_schema.dump(all_athletes)
        return athletes_schema.jsonify(a)

    return app
