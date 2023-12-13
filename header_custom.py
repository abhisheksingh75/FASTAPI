from fastapi import FastAPI, Header

app = FastAPI()

# In-memory database
books_db = [
    {"id": 1, "title": "1984", "author": "George Orwell"},
    {"id": 2, "title": "To Kill a Mockingbird", "author": "Harper Lee"}
]

@app.get("/books/")
async def list_books(custom_header: str = Header(None)):
    
    if custom_header:
        # Filter the books if custom_header is provided
        filtered_books = [book for book in books_db if custom_header.lower() in book["title"].lower()]
        return filtered_books
    else:
        # Return all books if no custom_header is provided
        return books_db
