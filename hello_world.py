# FastAPI app
from fastapi import FastAPI

app = FastAPI(title="Hello World App")

# Building an endpoint
@app.get("/")
async def read_root():
    return {"message": "Hello, World! I am FastAPI Application."}

# Handling requests - Endpoint to greet a user dynamically.
@app.get("/greet/{name}")
async def greet_user(name: str):
    
    greeting = f"Hello, {name}! Welcome to FastAPI."
    return {"message": greeting}

# To run the application, use Uvicorn:
# uvicorn main:app --reload
