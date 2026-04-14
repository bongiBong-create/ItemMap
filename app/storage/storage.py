import json

from app.core.config import path_to_data


def load_data():
    try:
        with open(str(path_to_data), "r", encodings="utf-8") as f:
            data = json.load(f)

            return data

    except FileNotFoundError:
        print("Неправильный путь")
        return None


def save_data():
    try:
        with open(str(path_to_data), "r", encodings="utf-8") as f:
            json.dump(f)

    except FileNotFoundError:
        print("Неправильный путь")

    return None