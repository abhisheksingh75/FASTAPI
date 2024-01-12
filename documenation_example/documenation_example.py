from fastapi import FastAPI
from pydantic import BaseModel

# Metadata Configuration
description = """
Book Library API allows users to manage a collection of books. 📚

## Features:
* **Add new books** to the library.
* **Retrieve all books** in the library.
* **Get details** of a specific book.
"""

app = FastAPI(
    title="Book Library API",
    description=description,
    version="1.0.0",
    terms_of_service="http://abc.com/terms/",
    contact={
        "name": "Library Administrator",
        "email": "lib@abc.com",
        "url": "http://library.abc.com/contact/"
    },
    license_info={
        "name": "Licensed Under R&D License",
        "url": "http://abc.com/license/"
    }
)

# Pydantic Model for Book Data
class Book(BaseModel):
    id: int
    title: str
    author: str
    isbn: str
    publication_year: int

# Endpoints for the Book Library API

@app.post("/books/", status_code=201, tags=["Books"])
async def add_book(book: Book):
    """
    Add a new book to the library.

    - **id**: Unique identifier for the book.
    - **title**: Title of the book.
    - **author**: Author of the book.
    - **isbn**: ISBN number of the book.
    - **publication_year**: Year of publication.
    """
    # Logic to add book to the database
    return {"message": "Book added successfully", "book": book}

@app.get("/books/", tags=["Books"])
async def get_books():
    """
    Retrieve a list of all books in the library.

    This endpoint returns an array of book objects.
    """
    # Logic to retrieve all books
    return [{"id": 1, "title": "2000", "author": "Ron Dill", "isbn": "1234567890", "publication_year": 1950}]

@app.get("/books/{book_id}", tags=["Books"])
async def get_book(book_id: int):
    """
    Retrieve details of a specific book by its ID.

    - **book_id**: The unique identifier of the book.
    """
    # Logic to retrieve a specific book
    return {"id": book_id, "title": "Brave red", "author": "Alexa", "isbn": "0987644321", "publication_year": 1940}
