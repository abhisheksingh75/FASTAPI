from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse

app = FastAPI()

# Mock database of books
books = {
    1: {"title": "Learning Python", "author": "Mark Lutz"},
    2: {"title": "JavaScript: The Good Parts", "author": "Douglas Crockford"},
}

# Custom Exception for Book Not Found
class BookNotFoundException(Exception):
    def __init__(self, book_id: int):
        self.message = f"Book with ID {book_id} not found"

@app.exception_handler(BookNotFoundException)
async def book_not_found_exception_handler(request: Request, exc: BookNotFoundException):
    return JSONResponse(content={"error": exc.message}, status_code=404)


@app.get("/book/{book_id}")
async def get_book(book_id: int):
    if book_id not in books:
        raise BookNotFoundException(book_id)
    return books[book_id]
