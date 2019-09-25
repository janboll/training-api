from training.extensions import db
from .response import (
    _error_validation,
    _error_not_found,
    _error_not_allowed,
    _notif_item_created,
)

from flask.views import MethodView
from flask import request
from flask_marshmallow import exceptions


class ApiGeneric(MethodView):
    def __init__(self, schema, model, query_mappings=[]):
        super().__init__()
        self.model = model
        self.schema_many = schema(many=True)
        self.schema_single = schema()
        self.query_mappings = query_mappings

    def _get_all_or_by_id(self, id):
        if id is None:
            all_items = self.model.query.all()
            return self.schema_many.jsonify(all_items)
        else:
            item = self.model.query.get(id)
            if item:
                return self.schema_single.jsonify(item)
            return _error_not_found(self.model.__name__, id)

    def _post_single_item(self):
        json_data = request.get_json()
        try:
            item = self.schema_single.load(json_data)
        except exceptions.ValidationError as e:
            return _error_validation(e)
        db.session.add(item)
        db.session.commit()
        return _notif_item_created(self.model.__name__)

    def _get_by_query(self):
        for query in self.query_mappings:
            param_dict = {key: request.args.get(key) for key in query["params"]}
            if min([param_dict[key] is not None for key in param_dict]):
                return param_dict, query["query_func"]

    def _query_by_param(self, query_tuple):
        func = query_tuple[1]
        # Todo: can raise type error...
        items = func(**query_tuple[0])
        return self.schema_many.jsonify(items)

    def get(self, id):
        param_dict = self._get_by_query()
        if param_dict:
            return self._query_by_param(param_dict)
        return self._get_all_or_by_id(id)

    def post(self):
        return self._post_single_item()


def register_api(blueprint, view, url, pk="id", pk_type="int"):
    view_func = view.as_view(url)
    blueprint.add_url_rule(
        url, defaults={pk: None}, view_func=view_func, methods=["GET"]
    )
    blueprint.add_url_rule(url, view_func=view_func, methods=["POST"])
    blueprint.add_url_rule(
        "{}/<{}:{}>".format(url, pk_type, pk), view_func=view_func, methods=["GET"]
    )
