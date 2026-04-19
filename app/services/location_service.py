from app.repository import location_repo


def create_location(name, description):
    existing = location_repo.get_location_by_name(name)

    if existing:
        raise ValueError("Локация уже существует")

    return location_repo.create_location(name, description)


def get_locations():
    return location_repo.get_locations()
