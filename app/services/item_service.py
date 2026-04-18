from app.models.item import create_item
from app.storage.storage import save_data


def add_item(data, name, location_id, description, aliases):
    item = create_item(name, location_id, aliases, description)
    data["items"].append(item)
    save_data(data)

    return item


def get_items(data):
    return data["items"]


def remove_item(data, item_id):
    data["items"] = [item for item in data["items"] if item["id"] != item_id]
    save_data(data)

    return item_id


def get_item_by_id(data, item_id):
    return next((item for item in data["items"] if item["id"] == item_id), None)


def get_item_by_name(data, name):
    return next((item for item in data["items"] if item["name"] == name), None)
