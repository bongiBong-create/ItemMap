from app.core.helpers import create_id


def create_location(name, description):
    return {
        "id": create_id(),
        "name": name,
        "description": description
    }
