def _notif_item_created(entity):
    return {"notification": "Item of type {} created.".format(entity)}, 201
