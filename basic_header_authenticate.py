from fastapi import FastAPI, Header, HTTPException

app = FastAPI()

# In-memory database (list of dictionaries)
books_db = [{"id": 1, "title": "1984", "author": "George Orwell"}, {"id": 2, "title": "To Kill a Mockingbird", "author": "Harper Lee"}]

@app.get("/books/")
async def list_books(token: str = Header(None)):
    if token != "YOUR_SECRET_TOKEN":
        raise HTTPException(status_code=401, detail="Unauthorized")
    return books_db
