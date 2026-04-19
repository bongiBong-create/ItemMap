from app.repository import location_repo, item_repo

def create_item(name, description, name_location):
    location = location_repo.get_location_by_name(name_location)

    if location is None:
        location = location_repo.create_location(name_location, "")

    return item_repo.create_item(name, location["id"], description)


def get_items():
    return item_repo.get_items()

#
# def remove_item(data, item_id):
#     data["items"] = [item for item in data["items"] if item["id"] != item_id]
#     save_data(data)
#
#     return item_id
