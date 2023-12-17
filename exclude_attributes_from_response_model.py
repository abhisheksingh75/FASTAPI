from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, Dict

app = FastAPI()

# Define the Pydantic model for a Book
class Book(BaseModel):
    title: str
    author: str
    year: Optional[int] = None
    internal_id: Optional[str] = None

# Mock in-memory database
book_db: Dict[int, Dict] = {
    1: {"title": "1984", "author": "George Orwell", "year": 1949, "internal_id": "B1"},
    2: {"title": "Brave New World", "author": "Aldous Huxley", "year": 1932, "internal_id": "B2"},
    3: {"title": "The Hitchhiker's Guide to the Galaxy", "author": "Douglas Adams", "year": 1979, "internal_id": "B3"}
}

# Function to get a book from the in-memory database
def get_book(book_id: int):
    return book_db.get(book_id)

@app.get("/books/{book_id}", response_model=Book, response_model_exclude={"internal_id"})
async def read_book(book_id: int):
    book = get_book(book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book
