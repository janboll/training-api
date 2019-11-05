import pytest

from werkzeug.exceptions import BadRequest

from training.views.generic import ApiGeneric
from training.extensions import db
from training.extensions import ma
from training import app


@pytest.fixture
def generic_api_instance():
    class TestModel(db.Model):
        __table_args__ = {'extend_existing': True}
        id = db.Column(db.Integer, primary_key=True)
        foo = db.Column(db.String)

    class TestSchema(ma.ModelSchema):
        class Meta:
            model = TestModel

    yield TestModel, TestSchema, ApiGeneric(TestSchema, TestModel)


@pytest.fixture
def default_test_request_context():
    with app.test_request_context() as request:
        yield request


def test__get_all_or_by_id_all(mocker, generic_api_instance, default_test_request_context):
    model, schema, api_instance = generic_api_instance
    model_mock = mocker.patch.object(api_instance, "model")
    model_mock.query.all.return_value = [model(id=321, foo="rab"), model(id=123, foo="bar")]
    response = api_instance._get_all_or_by_id(None)
    model_mock.query.all.assert_called_once_with()
    assert response.is_json is True
    assert len(response.get_json()) == 2
    assert response.get_json()[0]["id"] == 321
    assert response.get_json()[1]["id"] == 123


def test__get_all_or_by_id_id(mocker, generic_api_instance, default_test_request_context):
    model, schema, api_instance = generic_api_instance
    model_mock = mocker.patch.object(api_instance, "model")
    model_mock.query.get.return_value = model(id=123, foo="bar")
    response = api_instance._get_all_or_by_id(123)
    model_mock.query.get.assert_called_once_with(123)
    assert response.is_json is True
    assert response.get_json()["foo"] == "bar"
    assert response.get_json()["id"] == 123


def test__get_item_from_request_fail(generic_api_instance):
    model, schema, api_instance = generic_api_instance
    with app.test_request_context(json={"oof": "bar"}):
        try:
            api_instance._get_item_from_request()
        except BadRequest as e:
            message = e.description

    assert message == "Failed to validate sent object. {'oof': ['Unknown field.']}"


def test__get_item_from_request(generic_api_instance):
    model, schema, api_instance = generic_api_instance
    with app.test_request_context(json={"foo": "bar"}):
        item = api_instance._get_item_from_request()
        assert item.foo == "bar"


def test__post_single_item(mocker, generic_api_instance):
    model, schema, api_instance = generic_api_instance
    db.session.add = mocker.stub(name="db.session.add")
    db.session.commit = mocker.stub(name="db.session.commit")

    item = model()
    retVal = api_instance._post_single_item(item)

    db.session.add.assert_called_once_with(item)
    db.session.commit.assert_called_once()

    assert retVal[0]["notification"] == "Item of type {} created.".format(model.__name__)
    assert retVal[1] == 201
