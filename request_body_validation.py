from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

tags_metadata = [
    {
        "name": "Request body validation",
    }
]

app = FastAPI(openapi_tags=tags_metadata)

# "Database" to store books
books_db = []

class BookCreate(BaseModel):
    title: str
    author: str
    genre: str
    publication_year: int

class Book(BaseModel):
    title: str
    author: str
    genre: str
    publication_year: int

@app.post("/create_book_with_validation/")
async def create_book_with_validation(book: BookCreate):
    """
    Endpoint to create a book entry with validation.

    Parameters:
    - book: A Pydantic model representing the request body with attributes (title, author, genre, publication_year).

    Returns:
    - JSON response containing the details of the created book.

    Raises:
    - HTTPException with a 400 status code if the publication year is before 1500.
    """
    # Validation check: Ensure the publication year is after 1500
    if book.publication_year < 1500:
        raise HTTPException(status_code=400, detail="Publication year must be after 1500")

    # Create a new book instance
    new_book = Book(**book.dict())

    # Store the book in the "database"
    books_db.append(new_book)

    # Return the book details
    return new_book.dict()

@app.get("/get_all_books/")
async def get_all_books():
    """
    Endpoint to retrieve all books in the database.

    Returns:
    - JSON response containing details of all books.
    """
    return books_db
