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

    class AthleteSchema(ma.ModelSchema):
        class Meta:
            model = Athlete

    class PersonalBestsSchema(ma.ModelSchema):
        class Meta:
            model = PersonalBest

    athletes_schema = AthleteSchema(many=True)
    personalbestes_schema = PersonalBestsSchema(many=True)

    @app.route("/api/athletes/")
    def athletes():
        db.create_all()
        all_pbs = PersonalBest.query.all()
        p = personalbestes_schema.dump(all_pbs)
        all_athletes = Athlete.query.all( )
        a = athletes_schema.dump(all_athletes)
        print(a)
        print(p)
        return athletes_schema.jsonify(a)

    return app
