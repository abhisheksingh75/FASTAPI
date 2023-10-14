from fastapi import FastAPI, Cookie, Response

tags_metadata = [
    {
        "name": "Chapter 7 - Cookies Parameters"
    }
]

app = FastAPI(openapi_tags=tags_metadata)

# Set a cookie with a user ID
@app.get("/set_cookie/")
async def set_cookie(response: Response, user_id: str):
    response.set_cookie(key="user_id", value=user_id)
    return {"message": f"Cookie set for user {user_id}"}

# Retrieve user ID from the cookie
@app.get("/get_cookie/")
async def get_cookie(user_id: str = Cookie(None)):
    if user_id:
        return {"message": f"Welcome back, User {user_id}!"}
    else:
        return {"message": "Cookie not found. Please set the cookie."}

# Clear the user's session by deleting the cookie
@app.get("/clear_cookie/")
async def clear_cookie(response: Response):
    response.delete_cookie(key="user_id")
    return {"message": "Cookie deleted. User logged out."}
