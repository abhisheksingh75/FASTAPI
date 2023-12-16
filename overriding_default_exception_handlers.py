from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse

app = FastAPI()

# Overriding the default handler for HTTPException
@app.exception_handler(HTTPException)
async def custom_http_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(content={"custom error": exc.detail}, status_code=exc.status_code)

# Mock database of books
books = {
    1: {"title": "Learning Python", "author": "Mark Lutz"},
    2: {"title": "JavaScript: The Good Parts", "author": "Douglas Crockford"}
}

@app.get("/book/{book_id}")
async def get_book(book_id: int):
    if book_id not in books:
        raise HTTPException(status_code=404, detail="Book not found")
    return books[book_id]
