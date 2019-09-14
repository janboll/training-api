from training.model import Athlete, PersonalBest
from training.extensions import ma


class AthleteSchema(ma.ModelSchema):
    class Meta:
        model = Athlete

    personalbest = ma.List(ma.HyperlinkRelated("basic.personalbest"))

    _links = ma.Hyperlinks(
        {"self": ma.URLFor("basic.athlete", id="<id>")}
    )


class PersonalBestsSchema(ma.ModelSchema):
    class Meta:
        model = PersonalBest

    # Smart hyperlinking
    _links = ma.Hyperlinks(
        {"self": ma.URLFor("basic.personalbest", id="<id>")}
    )

athletes_schema = AthleteSchema(many=True)
personalbestes_schema = PersonalBestsSchema(many=True)
