from fastapi import FastAPI, Query
from pydantic import BaseModel

tags_metadata = [
    {
        "name": "Optional query parameters"
    }
]

app = FastAPI(openapi_tags=tags_metadata)

books = [
    {"title": "Book 1", "author": "Author A", "genre": "fantasy"},
    {"title": "Book 2", "author": "Author B", "genre": "mystery"},
    {"title": "Book 3", "author": "Author C", "genre": "sci-fi"}
]

class Book(BaseModel):
    title: str
    author: str
    genre: str

# Endpoint to retrieve a list of books with optional query parameters
@app.get("/books/")
async def get_books(
    skip: int = Query(0, title="Number of books to skip", description="Default: 0"),
    limit: int = Query(10, title="Number of books to retrieve", description="Default: 10"),
    genre: str = Query(None, title="Optional query parameter for filtering books by genre")
):
    """
    Retrieve a list of books with optional query parameters.

    Parameters:
    - skip: Number of books to skip (default: 0)
    - limit: Number of books to retrieve (default: 10)
    - genre: Optional query parameter for filtering books by genre

    Example Usage:
    - /books/?skip=5&limit=15&genre=mystery
    """

    # Apply optional filters
    filtered_books = [
        book for book in books if (genre is None or book["genre"] == genre)
    ]

    # Apply skip and limit
    result_books = filtered_books[skip : skip + limit]

    # Return the result
    return {"skip": skip, "limit": limit, "genre": genre, "books": result_books}
