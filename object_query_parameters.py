from fastapi import FastAPI, Query
from pydantic import BaseModel

app = FastAPI()

# Pydantic model representing object query parameters
class BookQueryParams(BaseModel):
    publication_year: int
    language: str

# In a real application, you might have a database and perform queries here
books = [
    {"title": "Book 1", "author": "Author A", "genre": "fantasy", "publication_year": 2021, "language": "english"},
    {"title": "Book 2", "author": "Author B", "genre": "mystery", "publication_year": 2022, "language": "spanish"},
    {"title": "Book 3", "author": "Author A", "genre": "sci-fi", "publication_year": 2022, "language": "english"}
]

# Endpoint to retrieve books using object query parameters
@app.get("/books/")
async def get_books(params: BookQueryParams):
    """
    Retrieve a list of books using object query parameters.

    Parameters:
    - params: Object query parameter representing book filters

    Example Usage:
    - /books/?publication_year=2022&language=english
    """

    # Apply filtering based on object query parameters
    filtered_books = [
        book for book in books
        if (params.publication_year is None or book["publication_year"] == params.publication_year)
           and (params.language is None or book["language"] == params.language)
    ]

    # Return the result
    return {"query_params": params.dict(), "books": filtered_books}
