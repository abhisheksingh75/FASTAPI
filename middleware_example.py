from fastapi import FastAPI, Request
from typing import List

app = FastAPI()

# Middleware to check and respond with custom headers
@app.middleware("http")
async def custom_header_middleware(request: Request, call_next):
    custom_header = request.headers.get('X-Custom-Request-Header', 'default_value')
    
    response = await call_next(request)
    
    response.headers['X-Custom-Response-Header'] = f"Processed: {custom_header}"
    return response

# Sample data
books_data = [
    {"title": "1984", "author": "George Orwell"},
    {"title": "To Kill a Mockingbird", "author": "Harper Lee"},
    {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald"}
]

# Endpoint to get a list of books
@app.get("/books", response_model=List[dict])
async def get_books():
    return books_data

# Run the server
# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="0.0.0.0", port=8000)
