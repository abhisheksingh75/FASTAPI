from fastapi import FastAPI, HTTPException, Query
from typing import Optional

app = FastAPI()

# A mock database of tech books
tech_books = {
    1: {"title": "Learning Python", "author": "Mark Lutz", "language": "Python"},
    2: {"title": "JavaScript: The Good Parts", "author": "Douglas Crockford", "language": "JavaScript"},
    3: {"title": "Clean Code", "author": "Robert C. Martin", "language": "General Programming"},
}

@app.get("/tech-book/{book_id}")
async def get_tech_book(book_id: int, language: Optional[str] = Query(None)):
    # Basic validation for book ID
    if book_id <= 0:
        raise HTTPException(status_code=400, detail="Invalid book ID")

    # Check if the book ID exists in our collection
    if book_id not in tech_books:
        raise HTTPException(status_code=404, detail="Tech book not found")

    # Get the book details
    book = tech_books[book_id]

    # Filter by language if specified
    if language and book["language"].lower() != language.lower():
        raise HTTPException(status_code=404, detail="Tech book not found for the specified language")

    # Return book details
    return book
