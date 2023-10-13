from fastapi import FastAPI
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    description: str


tags_metadata = [
    {
        "name": "Chapter 3 - Understanding Path Parameters"
    }
]

app = FastAPI(openapi_tags=tags_metadata)

@app.get("/")
async def BASE_PATH():
    return 'FastAPI Server is Running...'

@app.get("/items/basic_path/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}

@app.get("/items/default_value/{item_id}")
async def read_item(item_id: int = 0):
    return {"item_id": item_id}

@app.get("/multiple_path_params/users/{user_id}/items/{item_id}")
async def read_user_item(user_id: int, item_id: int):
    return {"user_id": user_id, "item_id": item_id}

@app.post("/items/object_path_params/{item_id}")
async def read_item(item_id: int, query_params: Item):
    return {"item_id": item_id, "item_details": query_params}