import json
import os
from app.core.config import path_to_data
from json import JSONDecodeError


def load_data():
    try:
        with open(path_to_data, "r", encoding="utf-8") as f:
            data = json.load(f)

            return data

    except (FileNotFoundError, JSONDecodeError):
        os.makedirs("data", exist_ok=True)

        data = {
            "locations": [],
            "items": [],
            "meta": []
        }

        save_data(data)

        return data


def save_data(data):
    with open(path_to_data, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)