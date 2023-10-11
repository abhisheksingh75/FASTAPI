from fastapi import FastAPI

tags_metadata = [
    {
        "name": "Chapter 1",
        "description": "Creating your first FastAPI Server",
    }
]

app = FastAPI(openapi_tags=tags_metadata)


@app.get("/")
async def root():
    return {"message": "Hello FastAPI! :)"}