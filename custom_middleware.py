from fastapi import FastAPI, Request
from starlette.middleware.base import BaseHTTPMiddleware
import time
import logging
import asyncio

app = FastAPI()

# Setting up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class RequestTimingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        start_time = time.perf_counter()
        response = await call_next(request)
        duration = time.perf_counter() - start_time
        logger.info(f"Request to {request.url.path} took {duration:.6f} seconds")
        return response

# Adding the middleware to the app
app.add_middleware(RequestTimingMiddleware)

# Sample endpoint with artificial delay
@app.get("/testing-middleware")
async def read_items():
    await asyncio.sleep(1.5)  # Delay for 1.5 seconds
    return {"message": "testing middleware"}

