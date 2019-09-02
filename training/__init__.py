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

    from training.model.Model import User

    class UserSchema(ma.ModelSchema):
        class Meta:
            model = User

    users_schema = UserSchema(many=True)

    @app.route("/api/users/")
    def users():
        db.create_all()
        all_users = User.query.all()
        a = users_schema.dump(all_users)
        return users_schema.jsonify(a)

    return app



