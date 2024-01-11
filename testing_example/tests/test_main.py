import sys
from pathlib import Path

# Add the parent directory to sys.path to find main.py
sys.path.append(str(Path(__file__).resolve().parent.parent))


import pytest
from fastapi.testclient import TestClient
from main import app

@pytest.fixture
def client():
    return TestClient(app)

def test_read_books(client):
    response = client.get("/books/")
    assert response.status_code == 200
    assert len(response.json()) == 2  # We initially have 2 books

@pytest.mark.parametrize("book", [
    {"title": "Titan", "author": "Ron Chernow"}, 
    {"title": "Medatall", "author": "Chris Whipple"}
])

def test_add_book(client, book):
    response = client.post("/books/", json=book)
    assert response.status_code == 200
    assert response.json() == book

def test_add_book_error(client):
    # Test with missing title
    response = client.post("/books/", json={"author": "Anonymous"})
    assert response.status_code == 400
    assert response.json() == {"detail": "Both title and author are required"}
