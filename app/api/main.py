from fastapi import FastAPI

from starlette.middleware.cors import CORSMiddleware
from app.models.schema import LocationCreate, ItemCreate
from app.services.location_service import add_location, get_locations, get_location_by_name
from app.services.item_service import get_items, add_item
from app.storage.storage import load_data

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def hello():
    return {"hello": "world"}


@app.post("/locations")
def create_location(payload: LocationCreate):
    data = load_data()

    location = add_location(data,
                            payload.name,
                            payload.description
                            )

    return location


@app.get("/locations")
def get_locations_list():
    data = load_data()

    locations = get_locations(data)

    return locations


@app.post("/items")
def create_item(payload: ItemCreate):
    data = load_data()
    location = get_location_by_name(data, payload.location)

    if location is None:
        location = add_location(data,
                                payload.location, "")

    item = add_item(data,
                    payload.name,
                    location["id"],
                    payload.description,
                    aliases=["", ""],
                    )

    return item


@app.get("/items")
def get_items_list():
    data = load_data()

    items = get_items(data)

    return items
