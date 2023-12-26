from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from database import Base

class Books(Base):
    __tablename__ = "books"
    
    id: int = Column(Integer, primary_key=True, index=True)
    title: str = Column(String, index=True)

class Authors(Base):
    __tablename__ = "authors"
    
    id: int = Column(Integer, primary_key=True, index=True)
    name: str = Column(String, index=True)
    is_primary: bool = Column(Boolean, index=True)
    book_id: int = Column(Integer, ForeignKey("books.id"))
