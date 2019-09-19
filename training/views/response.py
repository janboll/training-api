def _notif_item_created(entity):
    return {"notification": "Item of type {} created.".format(entity)}, 201


def _error_validation(e):
    return (
        {"error": "Failed to validate sent object.", "error_message": e.messages},
        400,
    )


def _error_not_found(entitiy, identifier):
    return (
        {
            "error": "Not found",
            "error_message": "{} with identifier {} not found.".format(
                entitiy, identifier
            ),
        },
        404,
    )


def _error_not_allowed(method):
    return (
        {
            "error": "Not Allowed",
            "error_message": "Method {} is not allowed here.".format(method),
        },
        405,
    )
