from app.models.item import create_item
from app.storage.storage import save_data


def add_item(data, name, location_id, aliases, description):
    location = next((location for location in data["locations"] if location["id"] == location_id),
                    None)

    if location is None:
        raise ValueError("Location not found")

    item = create_item(name, location_id, aliases, description)
    data["items"].append(item)
    save_data(data)

    return item


def remove_item(data, item_id):
    data["items"] = [item for item in data["items"] if item["id"] != item_id]
    save_data(data)

    return id


def get_item(data,  item_id):
    search_item = next((item for item in data["items"] if item["id"] == item_id), None)

    return search_item
