from fastapi import FastAPI, Request
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.errors import RateLimitExceeded
from slowapi.util import get_remote_address

app = FastAPI()
limiter = Limiter(key_func=get_remote_address)

# Mock data for books
books_data = [
    {"title": "1984", "author": "Boris Pasternak"},
    {"title": "New Universe", "author": "Stephen Hawking"},
    {"title": "testing 451", "author": "L. Frank Baum"},
]

# Apply rate limiting to the books endpoint
@app.get("/books")
@limiter.limit("5/minute")
async def read_books(request: Request):  # Include request: Request here
    return {"books": books_data}

# Handle rate limit exceeded
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)