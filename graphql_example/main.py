import strawberry
from typing import List, Optional
from pydantic import BaseModel
from uuid import uuid4, UUID
from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter

# Pydantic model for book data
class BookModel(BaseModel):
    id: Optional[UUID] = None
    title: str
    author: str

# In-memory database
db: List[BookModel] = []

# Strawberry GraphQL Book Type
@strawberry.type
class Book:
    id: UUID
    title: str
    author: str

# GraphQL Query
@strawberry.type
class Query:
    @strawberry.field
    def list_books(self) -> List[Book]:
        return db

# GraphQL Mutations
@strawberry.type
class Mutation:
    @strawberry.mutation
    def create_book(self, title: str, author: str) -> Book:
        book = BookModel(id=uuid4(), title=title, author=author)
        db.append(book)
        return book

    @strawberry.mutation
    def update_book(self, id: UUID, title: str, author: str) -> Optional[Book]:
        for book in db:
            if book.id == id:
                book.title = title
                book.author = author
                return book
        return None

    @strawberry.mutation
    def delete_book(self, id: UUID) -> bool:
        global db
        db = [book for book in db if book.id != id]
        return True

# Creating the Strawberry Schema
schema = strawberry.Schema(query=Query, mutation=Mutation)

# FastAPI Integration
app = FastAPI()
app.include_router(GraphQLRouter(schema), prefix="/graphql")
