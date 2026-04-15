from app.models.location import create_location
from app.storage.storage import save_data


def add_location(data, name, description):
    location = create_location(name, description)
    data["locations"].append(location)
    save_data(data)

    print(f"{name} - создана")
    return location

def get_locations(data):
    for location in data["locations"]:
        print(location)