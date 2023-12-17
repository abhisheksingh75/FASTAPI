from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, Dict

app = FastAPI()

# Define the Pydantic model for a Book
class Book(BaseModel):
    title: str
    author: str
    year: Optional[int] = None

# Mock database for the example
fake_book_db: Dict[int, Book] = {
    1: Book(title="1984", author="George Orwell", year=1949),
    2: Book(title="Brave New World", author="Aldous Huxley", year=1932)
}

@app.get("/books/{book_id}", response_model=Book)
async def read_book(book_id: int):
    if book_id not in fake_book_db:
        raise HTTPException(status_code=404, detail="Book not found")
    return fake_book_db[book_id]

@app.post("/books/", response_model=Book, status_code=201)
async def create_book(book: Book):
    next_id = max(fake_book_db.keys()) + 1
    fake_book_db[next_id] = book
    return book
