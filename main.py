from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from database import Base, engine, SessionLocal
from models import Book
from schemas import BookCreate

# Create FastAPI application
app = FastAPI(title="Digital Book Library API")

# Create database tables automatically
Base.metadata.create_all(bind=engine)

# Database connection dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Home Route
@app.get("/")
def home():
    return {
        "message": "Library API Running Successfully"
    }

# Add New Book
@app.post("/api/v1/books/")
def add_book(
    book: BookCreate,
    db: Session = Depends(get_db)
):
    new_book = Book(
        title=book.title,
        author=book.author,
        is_borrowed=book.is_borrowed
    )

    db.add(new_book)
    db.commit()
    db.refresh(new_book)

    return new_book

# Get All Books
@app.get("/api/v1/books/")
def get_books(
    db: Session = Depends(get_db)
):
    books = db.query(Book).all()
    return books