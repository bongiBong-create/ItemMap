from app.models.location import create_location
from app.storage.storage import save_data


def add_location(data, name, description):
    location = create_location(name, description)
    data["locations"].append(location)
    save_data(data)

    return location


def get_locations(data):
    return data["locations"]


def get_location_by_id(data, location_id):
    return next((location for location in data["locations"] if location["id"] == location_id),
                None)


def get_location_by_name(data, name):
    location = next((location for location in data["locations"] if location["name"] == name),
                    None)

    if location is None:
        new_location = add_location(data, name, description="")
        return new_location

    return location
