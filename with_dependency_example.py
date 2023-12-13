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


def get_db():
    try:
        db = books_db
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
