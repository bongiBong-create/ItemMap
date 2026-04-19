from app.core.helpers import create_id
from app.storage.storage import load_data, save_data


def create_item(name, location_id, description):
    data = load_data()

    item = {
        "id": create_id(),
        "name": name,
        "location_id": location_id,
        "description": description,

    }

    data["items"].append(item)
    save_data(data)

    return item

def get_items():
    data = load_data()

    return data["items"]

def get_item_by_id(item_id):
    data = load_data()

    return next((item for item in data["items"] if item["id"] == item_id), None)


def get_item_by_name(name):
    data = load_data()

    return next((item for item in data["items"] if item["name"] == name), None)
