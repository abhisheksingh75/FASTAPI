from fastapi import FastAPI, Response
from fastapi.responses import JSONResponse

app = FastAPI()

# In-memory database
books_db = [{"id": 1, "title": "1984", "author": "George Orwell"}, {"id": 2, "title": "To Kill a Mockingbird", "author": "Harper Lee"}]

@app.get("/books/", response_class=JSONResponse)
async def list_books():
    return books_db
