from . import app
from werkzeug.exceptions import NotFound, BadRequest


@app.errorhandler(BadRequest)
def error_validation(error: BadRequest):
    return {"error": "Bad Request", "error_message": error.description}, 400


@app.errorhandler(NotFound)
def error_not_found(error: NotFound):
    return {"error": "Not found", "error_message": error.description}, 404
