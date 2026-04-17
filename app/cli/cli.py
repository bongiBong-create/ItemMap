from app.services.item_service import add_item, get_item_by_name, remove_item, get_items, get_location_by_id
from app.services.location_service import add_location, get_location_by_name, get_locations
from app.storage.storage import load_data

data = load_data()


def cli():
    try:
        while True:

            cmd = input(
                "Введите операцию\nadd-location\nadd-item\nremove-item\nlocations-list\nitems-list\n")

            if cmd == "add-location":
                name_location = input("Введите название локации\n")
                description_location = input("Введите описание\n")

                location = add_location(data, name_location, description_location)

                print(f"{location['name']} - создан")
            elif cmd == "add-item":
                name_item = input("Введите название item\n")
                description_item = input("Введите описание item\n")
                name_location = input("Введите существующую локацию\n")
                location = get_location_by_name(data, name_location)

                item = add_item(data, name_item, location["id"], description_item)

                print(f"{name_location} - создан")
                print(f"{item['name']} - создан")

            elif cmd == "remove-item":
                name_item = input("Введите название предмета")
                item = get_item_by_name(data, name_item)

                if item is None:
                    print("такого предмета не существует")

                remove_item(data, item["id"])
                print("предмет удален")

            elif cmd == "locations-list":
                locations = get_locations(data)
                if locations:
                    for location in locations:
                        print(f"{location['name']}\n")
                else:
                    print("Список пуст")
            elif cmd == "items-list":
                items = get_items(data)

                if items:
                    for item in items:
                        location = get_location_by_id(data, item["location_id"])
                        print(f"{item['name']} - лежит в {location['name']}")
                else:
                    print("Список пуст")
    except KeyboardInterrupt:
        print("До свидания\n")
