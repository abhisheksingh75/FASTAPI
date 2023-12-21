# main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://alpha.com", "http://127.0.0.1:5500"], # Replace with the allowed origin
    allow_credentials=True,
    allow_methods=["GET", "POST"], # Allowed methods
    allow_headers=["Content-Type"], # Allowed headers
)

# Sample endpoint
@app.get("/cors-testing")
async def read_items():
    return {"message": "cors-testing"}
