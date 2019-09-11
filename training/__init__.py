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

        personalbests = ma.List(ma.HyperlinkRelated("personal_best"))

        _links = ma.Hyperlinks(
            {"self": ma.URLFor("athletes", id="<id>")}
        )

    class PersonalBestsSchema(ma.ModelSchema):
        class Meta:
            model = PersonalBest

        # Smart hyperlinking
        _links = ma.Hyperlinks(
            {"self": ma.URLFor("personal_best", id="<id>")}
        )

    athletes_schema = AthleteSchema(many=True)
    personalbestes_schema = PersonalBestsSchema(many=True)

    @app.route("/api/athletes/")
    def athletes():
        db.create_all()
        all_athletes = Athlete.query.all()
        print(all_athletes)
        a = athletes_schema.dump(all_athletes)
        print(a)
        return athletes_schema.jsonify(a)

    @app.route("/api/personal_best")
    def personal_best():
        pass

    return app
