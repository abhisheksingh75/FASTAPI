from fastapi import FastAPI

tags_metadata = [
    {
        "name": "Chapter 1",
        "description": "Creating your first FastAPI Server",
    }
]

app = FastAPI(openapi_tags=tags_metadata)


#Here, @app.get("/") is a decorator that specifies that this function should handle HTTP GET requests at the root path ("/").
@app.get("/")
async def root():
    return {"message": "Hello FastAPI! :)"}