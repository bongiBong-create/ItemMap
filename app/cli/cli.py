from app.services.item_service import add_item, get_items
from app.services.location_service import add_location, get_locations
from app.storage.storage import load_data

data = load_data()


def cli():
    try:
        while True:
            cmd = int(input(
                "Введите число операции\n1. Создать локацию\n2. Добавить предмет в локацию\n3. Удалить локацию\n4. Список локаций\n5. Список предметов\n"))

            if cmd == 1:
                name_location = input("Введите название локации\n")
                description_location = input("Введите описание\n")

                location = add_location(data, name_location, description_location)

                name_item = input("Введите название предмета\n")
                description_item = input("Введите описание предмета\n")

                item = add_item(data, name_item, location["id"], ["predmet1"], description_item)
                print(f"{item["name"]} - предмет успешно создан")
            elif cmd == 4:
                get_locations(data)
            elif cmd == 5:
                get_items(data)
    except KeyboardInterrupt:
        print("До свидания\n")
