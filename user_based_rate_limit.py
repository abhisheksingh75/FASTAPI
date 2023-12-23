from fastapi import FastAPI, Depends, HTTPException, Request
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.errors import RateLimitExceeded
from slowapi.util import get_remote_address

app = FastAPI()
limiter = Limiter(key_func=lambda: Depends(get_current_user))

# Mock function to simulate user authentication
async def get_current_user():
    return "user_id_123"  # In real-world, return authenticated user's ID

# Add the limiter to the app state before the route definitions
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

@app.get("/books")
@limiter.limit("5/minute", key_func=lambda: Depends(get_current_user))
async def read_books(request: Request):
    return {"books": ["1984", "Brave New World"]}
