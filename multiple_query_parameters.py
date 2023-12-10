from fastapi import FastAPI

tags_metadata = [
    {
        "name": "multiple query parameters"
    }
]

app = FastAPI(openapi_tags=tags_metadata)

# Example: Book model using Pydantic
from pydantic import BaseModel

# In a real application, you might have a database and perform queries here
books = [
        {"title": "Book 1", "author": "Author A", "genre": "fantasy", "publication_year": 2021, "language": "english"},
        {"title": "Book 2", "author": "Author B", "genre": "mystery", "publication_year": 2022, "language": "spanish"},
        {"title": "Book 3", "author": "Author A", "genre": "sci-fi", "publication_year": 2022, "language": "english"}
    ]

class Book(BaseModel):
    title: str
    author: str
    genre: str
    publication_year: int
    language: str

# Endpoint to retrieve a list of books with custom filters
@app.get("/books/")
async def get_books(publication_year: int = None, language: str = None):
    """
    Retrieve a list of books with custom filters.

    Parameters:
    - publication_year: Optional query parameter for filtering books by publication year
    - language: Optional query parameter for filtering books by language

    Example Usage:
    - /books/?publication_year=2022&language=english
    """
   

    # Apply multiple filters
    filtered_books = [
        book for book in books
        if (publication_year is None or book["publication_year"] == publication_year)
        and (language is None or book["language"] == language)
    ]

    # Return the result
    return {"publication_year": publication_year, "language": language, "books": filtered_books}
