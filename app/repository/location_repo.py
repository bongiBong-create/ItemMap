from app.core.helpers import create_id
from app.storage.storage import load_data, save_data


def create_location(name, description):
    data = load_data()

    location = {
        "id": create_id(),
        "name": name,
        "description": description
    }

    data["locations"].append(location)
    save_data(data)

    return location


def get_locations():
    data = load_data()

    return data["locations"]


def get_location_by_name(name):
    data = load_data()

    location = next((location for location in data["locations"] if location["name"] == name),
                    None)
    return location


def get_location_by_id(location_id):
    data = load_data()

    return next((location for location in data["locations"] if location["id"] == location_id),
                None)
