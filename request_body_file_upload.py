from fastapi import FastAPI, Form, File, UploadFile
from pydantic import BaseModel

app = FastAPI()

class BookDetails(BaseModel):
    title: str
    author: str
    genre: str
    publication_year: int

@app.post("/books/")
async def create_book_with_cover(
    book_details: BookDetails = Form(...),
    cover_image: UploadFile = File(...)
):
    """
    Endpoint to create a book entry with optional cover image.

    Parameters:
    - book_details: JSON data representing book details, received as a Form parameter.
    - cover_image: Optional UploadFile representing the book cover image.

    Returns:
    - JSON response containing details of the created book.
    """
    # Process book details
    book = {
        "title": book_details.title,
        "author": book_details.author,
        "genre": book_details.genre,
        "publication_year": book_details.publication_year,
    }

    # Process cover image if provided
    if cover_image:
        # Save or process the cover image as needed
        # In this example, we just store the filename
        cover_filename = cover_image.filename
        book["cover_image"] = cover_filename

    # Save book details (in a database, for example)
    # In a real application, this is where you would persist the data

    return book
