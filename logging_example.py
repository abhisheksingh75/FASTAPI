import logging
from fastapi import FastAPI

tags_metadata = [
    {
        "name": "Loggin Application",
    }
]

app = FastAPI(openapi_tags=tags_metadata)

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

@app.get("/")
async def read_root():
    logger.info("Root endpoint accessed")
    return {"Hello": "World"}
