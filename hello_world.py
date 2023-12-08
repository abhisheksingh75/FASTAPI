# FastAPI app
from fastapi import FastAPI

tags_metadata = [
    {
        "name": "Hello World Application",
    }
]

app = FastAPI(openapi_tags=tags_metadata)

# Building an endpoint
@app.get("/")
async def read_root():
    return {"message": "Hello, World! I am FastAPI Application."}

# Handling requests - Endpoint to greet a user dynamically.
@app.get("/greet/{name}")
async def greet_user(name: str):
    
    greeting = f"Hello, {name}! Welcome to FastAPI."
    return {"message": greeting}