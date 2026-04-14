from app.models.item import create_item


def add_item(name, location_id, aliases, description):
    item = create_item(name, location_id, aliases, description)

    return item

