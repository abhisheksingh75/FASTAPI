from fastapi import FastAPI
from pydantic import BaseModel

tags_metadata = [
    {
        "name": "Chapter 4 - Working with Query Parameters"
    }
]

app = FastAPI(openapi_tags=tags_metadata)

class Filter(BaseModel):
    min_price: float
    category: str

@app.get("/items/basic/")
async def read_items_basic(skip: int = 0, limit: int = 10):
    return {"skip": skip, "limit": limit}

@app.get("/items/optional/")
async def read_items_optional(skip: int = 0, limit: int = 10):
    return {"skip": skip, "limit": limit}

@app.get("/items/object/")
async def read_items_object(filter_params: Filter):
    return {"filter_params": filter_params}
