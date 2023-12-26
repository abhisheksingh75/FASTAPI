from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from typing import List, Annotated 
import models 
from database import engine, SessionLocal
from sqlalchemy.orm import Session

app = FastAPI()
models.Base.metadata.create_all(bind=engine)

class AuthorBase(BaseModel):
    name: str
    is_primary: bool

class Book(BaseModel):
    title: str
    authors: List[AuthorBase]

def get_db():
    db = SessionLocal() 
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]

@app.post("/books/", response_model=Book)
async def create_book(book: Book, db: Session = Depends(get_db)):
    db_book = models.Books(title=book.title)
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    db_authors = []
    for author in book.authors:
        db_author = models.Authors(**author.dict(), book_id=db_book.id)
        db.add(db_author)
        db_authors.append(db_author)
    db.commit()
    db.refresh(db_book)
    for db_author in db_authors:
        db.refresh(db_author)
    return {
        **db_book.__dict__,
        "authors": [db_author.__dict__ for db_author in db_authors],
    }


@app.get("/books/", response_model=List[Book])
def read_books(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    db_books = db.query(models.Books).offset(skip).limit(limit).all()
    result = []
    for db_book in db_books:
        db_authors = db.query(models.Authors).filter(models.Authors.book_id == db_book.id).all()
        book = {
            "title": db_book.title,
            "authors": [{"name": author.name, "is_primary": author.is_primary} for author in db_authors]
        }
        result.append(book)
    return result