from fastapi import FastAPI
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.errors import RateLimitExceeded
from slowapi.util import get_remote_address

# Initialize FastAPI app and Limiter
app = FastAPI()
limiter = Limiter(key_func=get_remote_address)

# Apply global rate limit to all endpoints
app.add_middleware(limiter.middleware, limit="5/minute")

# Example endpoint 1: Books
@app.get("/books")
async def read_books():
    return {"books": ["1984", "Brave New World"]}

# Example endpoint 2: Authors
@app.get("/authors")
async def read_authors():
    return {"authors": ["George Orwell", "Aldous Huxley"]}

# Handle rate limit exceeded
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)
