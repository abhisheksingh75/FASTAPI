from fastapi import FastAPI
from pydantic import BaseModel

tags_metadata = [
    {
        "name": "Chapter 10 - Customizing Response Models and Status Codes"
    }
]

app = FastAPI(openapi_tags=tags_metadata)

# Sample data
items = {
    1: {"name": "Item 1", "price": 10.99},
    2: {"name": "Item 2", "price": 19.99},
}

# Pydantic model for an item
class Item(BaseModel):
    name: str
    price: float


@app.get("/define_response_model/items/{item_id}", response_model=Item)
async def define_response_model(item_id: int):
    item_data = items.get(item_id)
    return item_data


@app.get("/exclude_attributes_from_response/items/{item_id}", response_model=Item, response_model_exclude={"price"})
async def exclude_attributes_from_response(item_id: int):
    item_data = items.get(item_id)
    return item_data


@app.post("/customize_status_code_for_item_create/items/", response_model=Item, status_code=201)
async def customize_status_code_for_item_create(item: Item):
    # Process item creation
    return item
