from app.models.item import create_item
from app.storage.storage import save_data


def add_item(data, name, location_id, aliases, description):
    location = next((location for location in data["locations"] if location["id"] == location_id), None)

    if location is None:
        print("Такой локации не существует")
        return None

    item = create_item(name, location_id, aliases, description)
    data["items"].append(item)
    save_data(data)

    return item


def remove_item(data, id):
    data["items"] = [item for item in data["items"] if item["id"] != id]
    save_data(data)
    print("Предмет удален")


def get_item(data, id):
    item = next((item for item in data["items"] if item["id"] == id), None)

    return item

def get_items(data):
    for item in data["items"]:
        print(item)