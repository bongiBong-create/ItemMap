from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.schemas.location import LocationCreate
from app.schemas.item import ItemCreate
from app.services import location_service, item_service

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/locations")
def create_location(payload: LocationCreate):
    return location_service.create_location(payload.name, payload.description)


@app.get("/locations")
def get_locations_list():
    return location_service.get_locations()


@app.post("/items")
def create_item(payload: ItemCreate):
    return item_service.create_item(payload.name, payload.description, payload.location)


@app.get("/items")
def get_items_list():
    return item_service.get_items()
