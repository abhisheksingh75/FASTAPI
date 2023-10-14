from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse


tags_metadata = [
    {
        "name": "Chapter 9 - Dealing with Errors in FastAPI"
    }
]

app = FastAPI(openapi_tags=tags_metadata)


# Raising an HTTPException
users = {"alice": "password123"}

@app.post("/user/login")
async def standard_exception(username: str, password: str):
    if username not in users or users[username] != password:
        raise HTTPException(status_code=401, detail="Authentication failed")
    return {"message": "Login successful"}



# Custom Exception Handling
class CustomException(Exception):
    def __init__(self, message: str):
        self.message = message

@app.exception_handler(CustomException)
async def custom_exception_handler(request: Request, exc: CustomException):
    return JSONResponse(content={"custom error": exc.message}, status_code=400)


@app.get("/custom_exception")
async def trigger_custom_exception():
    raise CustomException("This is a custom exception")



# Overriding Default Exception Handlers
@app.exception_handler(HTTPException)
async def custom_http_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(content={"override custom error": exc.detail}, status_code=exc.status_code)

@app.get("/Overriding_http_exception/{item_id}")
async def Overriding_http_exception(item_id: int):
    if item_id < 0:
        raise HTTPException(status_code=400, detail="Item ID must be a positive integer")
    return {"item_id": item_id}

