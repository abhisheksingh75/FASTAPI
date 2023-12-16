from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse

app = FastAPI()

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
