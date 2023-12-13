from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# In-memory database
books_db = [{"id": 1, "title": "1984", "author": "George Orwell"}, {"id": 2, "title": "To Kill a Mockingbird", "author": "Harper Lee"}]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://example.com"],  # Specify allowed origins
    allow_credentials=True,
    allow_methods=["GET", "POST"],  # Restrict to certain HTTP methods
    allow_headers=["*"],
)

@app.get("/books1/")
async def list_books():
    return books_db
