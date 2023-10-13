from fastapi import FastAPI
from pydantic import BaseModel

tags_metadata = [
    {
        "name": "Chapter 5 - Handling Request Body"
    }
]

app = FastAPI(openapi_tags=tags_metadata)

class ItemCreate(BaseModel):
    name: str
    description: str
    price: float

@app.post("/items/")
async def create_item(item: ItemCreate):
    # Process the incoming item data
    # Example: Save it to a database
    return {"item": item}
