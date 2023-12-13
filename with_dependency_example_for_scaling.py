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


def get_db():
    db = books_db
    try:
        log_transaction("Database access")
        if len(db) > 100:
            raise Exception("Database overload")
        yield db
    finally:
        pass


@app.post("/create-book/")
def create_book(book: Book, db: list = Depends(get_db)):
    db.append(book.dict())
    return {"message": "Book added successfully"}

@app.get("/books/")
def get_books(db: list = Depends(get_db)):
    return db