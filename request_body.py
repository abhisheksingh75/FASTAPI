from fastapi import FastAPI
from pydantic import BaseModel

tags_metadata = [
    {
        "name": "Request body",
    }
]

app = FastAPI(openapi_tags=tags_metadata)


# Sample array to store books (simulating a database)
books_db = []

# Pydantic model representing the expected structure of incoming data (request body)
class BookCreate(BaseModel):
    title: str
    author: str
    genre: str
    publication_year: int

# FastAPI endpoint for handling HTTP POST requests at the path "/books/"
@app.post("/books/")
async def create_book(book: BookCreate):
    """
    Endpoint to create a book entry.

    Parameters:
    - book: A Pydantic model representing the request body with attributes (title, author, genre, publication_year).

    Returns:
    - JSON response containing the details of the created book.
    """
    # Insert the book into the array (simulating a database)
    books_db.append(book.dict())

    return {
        "title": book.title,
        "author": book.author,
        "genre": book.genre,
        "publication_year": book.publication_year
    }

# FastAPI endpoint for handling HTTP GET requests at the path "/books/"
@app.get("/get_books/")
async def get_books():
    """
    Endpoint to retrieve all books.

    Returns:
    - JSON response containing the list of books.
    """
    return {"books": books_db}
