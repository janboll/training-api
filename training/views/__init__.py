

def _validation_error_response(e):
    return {"error": "Failed to validate sent object.", "error_message": e.messages}, 400


def _not_found_error(entitiy, identifier):
    return {"error": "Not found", "error_message": "{} with identifier {} not found.".format(entitiy, identifier)}, 404
