from training.extensions import db
from .response import _error_validation, _error_not_found, _error_not_allowed, _notif_item_created

from flask_marshmallow import exceptions


def _load_and_insert(schema, request):
    json_data = request.get_json()
    try:
        item = schema.load(json_data)
    except exceptions.ValidationError as e:
        return _error_validation(e)
    db.session.add(item)
    db.session.commit()


def _entity_default_endpoint(model, schema, request):
    if request.method == "POST":
        _load_and_insert(schema(), request)
        return _notif_item_created(model.__name__)
    elif request.method == "GET":
        all_items = model.query.all()
        return schema(many=True).jsonify(all_items)
    else:
        return _error_not_allowed(request.method)


def _entity_specific_endpoint(model, schema, id):
        item = model.query.get(id)
        if item:
            return schema().jsonify(item)
        return _error_not_found(model.__name__, id)
