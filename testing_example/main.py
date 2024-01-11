# main.py

from fastapi import FastAPI
from typing import List

app = FastAPI()

books = [
            {"title": "Titan", "author": "Ron Chernow"}, 
            {"title": "Medatall", "author": "Chris Whipple"}
        ]

@app.get("/books/", response_model=List[dict])
async def read_books():
    return books

@app.post("/books/", response_model=dict)
async def add_book(book: dict):
    books.append(book)
    return book
