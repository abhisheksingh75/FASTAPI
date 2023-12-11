from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

tags_metadata = [
    {
        "name": "Default body example",
    }
]

app = FastAPI(openapi_tags=tags_metadata)

class BookDetails(BaseModel):
    title: str
    author: str
    genre: str
    publication_year: int = 2022

# In-memory "database" as a list
books_db = []

@app.post("/books/")
async def create_book(book_details: BookDetails):
    # Process book details
    book = {
        "title": book_details.title,
        "author": book_details.author,
        "genre": book_details.genre,
        "publication_year": book_details.publication_year,
    }

    # Save book details to the in-memory database
    books_db.append(book)

    return book

@app.get("/books/", response_model=List[BookDetails])
async def get_all_books():
    # Return all books from the in-memory database
    return books_db
