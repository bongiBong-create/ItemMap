from app.core.helpers import create_id, get_datetime


def create_item(name, location_id, aliases, description):
    return {
        "id": create_id(),
        "name": name,
        "location_id": location_id,
        "aliases": aliases,
        "description": description,
        "created_at": get_datetime()
    }
