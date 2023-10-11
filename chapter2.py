#import FastAPI and create an instance of the FastAPI app:
from fastapi import FastAPI
from typing import List

tags_metadata = [
    {
        "name": "Chapter 2 - FastAPI Data Types"
    }
]

app = FastAPI(openapi_tags=tags_metadata)

@app.get("/")
async def base_route():
    return "Hi, I am Running..."


#Here, item_id is a path parameter that is of type int.
@app.get("/items/integer/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}

#Here, item_id is a path parameter that is of type string.
@app.get("/items/string/{item_id}")
async def read_item(item_id: str):
    return {"item_id": item_id}

#Here, a and b are query parameters that are of type fload.
@app.get("/calculate/float/")
async def calculate(a: float, b: float):
    result = a + b
    return {"result": result}

# Here, enabled is a query parameter that is of type boolean.
@app.get("/status/boolean/")
async def get_status(enabled: bool):
    return {"enabled": enabled}

# Here, items is a query parameter that is of type list.
@app.post("/create_items/list/")
async def create_items(items: List[str]):
    return {"items": items}

# Here, user_data is a body parameter that is of type dictionary.
@app.post("/create_user/dictionary/")
async def create_user(user_data: dict):
    return {"user_data": user_data}