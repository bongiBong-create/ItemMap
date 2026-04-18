from pydantic import BaseModel

class LocationCreate(BaseModel):
    name: str
    description:str

class ItemCreate(BaseModel):
    name:str
    description:str
    location: str
