# routes.py
from fastapi import APIRouter, HTTPException
from models.books import Book
from config.database import collection_name 
from schema.schemas import list_serial, individual_serial
from bson import ObjectId

router = APIRouter()

@router.get("/books")
async def get_books():
    books = list_serial(collection_name.find())
    return books

@router.post("/books")
async def post_book(book: Book):
    _id = collection_name.insert_one(dict(book)).inserted_id
    book_data = collection_name.find_one({"_id": _id})
    return individual_serial(book_data)

@router.put("/books/{id}")
async def update_book(id: str, book: Book):
    if not collection_name.find_one({"_id": ObjectId(id)}):
        raise HTTPException(status_code=404, detail=f"Book with id {id} not found")

    collection_name.update_one({"_id": ObjectId(id)}, {"$set": dict(book)})
    updated_book = collection_name.find_one({"_id": ObjectId(id)})
    return individual_serial(updated_book)

@router.delete("/books/{id}")
async def delete_book(id: str):
    if not collection_name.find_one({"_id": ObjectId(id)}):
        raise HTTPException(status_code=404, detail=f"Book with id {id} not found")

    collection_name.delete_one({"_id": ObjectId(id)})
    return {"status": "Book deleted successfully"}
