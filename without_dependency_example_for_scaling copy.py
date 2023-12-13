from fastapi import FastAPI, Depends
from pydantic import BaseModel

# Define the Book model using Pydantic
class Book(BaseModel):
    id: int
    title: str
    author: str

# In-memory database (a simple list to store books)
books_db = []

app = FastAPI()

def log_transaction(message: str):
    # In a real application, you might want to write this to a log file or use a logging library
    print(f"Transaction Log: {message}")

def handle_database_error(error: Exception):
    # In a real application, you might want to log this error and perhaps send a notification
    print(f"Database Error: {error}")


@app.post("/create-book/")
def create_book(book: Book):
    try:
        # Additional logic for each database interaction
        log_transaction("Adding a new book")
        books_db.append(book.dict())
        if len(books_db) > 100:
            raise Exception("Database overload")
    except Exception as e:
        handle_database_error(e)
    return {"message": "Book added successfully"}

@app.get("/books/")
def get_books():
    try:
        log_transaction("Fetching all books")
        if len(books_db) > 100:
            raise Exception("Database overload")
        return books_db
    except Exception as e:
        handle_database_error(e)
