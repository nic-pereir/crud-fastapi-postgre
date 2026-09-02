from fastapi import Depends, FastAPI, HTTPException, status
from sqlalchemy.orm import Session
import crud
import models
import schemas
from database import Base, engine, get_db

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Book API - Library")

# BOOKS

@app.get("/books", response_model=list[schemas.BookOut])
def list_books(db: Session = Depends(get_db)):
    return crud.get_books(db)


@app.get("/books/{book_id}", response_model=schemas.BookOut)
def read_book(book_id: int, db: Session = Depends(get_db)):
    book = crud.get_book(db, book_id)
    if book is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")
    return book


@app.post("/books", response_model=schemas.BookOut, status_code=status.HTTP_201_CREATED)
def create_book(book: schemas.BookCreate, db: Session = Depends(get_db)):
    return crud.create_book(db, book)


@app.put("/books/{book_id}", response_model=schemas.BookOut)
def update_book(book_id: int, book: schemas.BookCreate, db: Session = Depends(get_db)):
    updated = crud.update_book(db, book_id, book)
    if updated is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")
    return updated


@app.delete("/books/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_book(book_id: int, db: Session = Depends(get_db)):
    deleted = crud.delete_book(db, book_id)
    if deleted is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")
    return None


# AUTHORS

@app.get("/authors", response_model=list[schemas.AuthorOut])
def list_authors(db: Session = Depends(get_db)):
    return crud.get_authors(db)


@app.get("/authors/{author_id}", response_model=schemas.AuthorOut)
def read_author(author_id: int, db: Session = Depends(get_db)):
    author = crud.get_author(db, author_id)
    if author is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Author not found")
    return author


@app.post("/authors", response_model=schemas.AuthorOut, status_code=status.HTTP_201_CREATED)
def create_author(author: schemas.AuthorCreate, db: Session = Depends(get_db)):
    return crud.create_author(db, author)


@app.put("/authors/{author_id}", response_model=schemas.AuthorOut)
def update_author(author_id: int, author: schemas.AuthorCreate, db: Session = Depends(get_db)):
    updated = crud.update_author(db, author_id, author)
    if updated is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Author not found")
    return updated


@app.delete("/authors/{author_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_author(author_id: int, db: Session = Depends(get_db)):
    deleted = crud.delete_author(db, author_id)
    if deleted is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Author not found")
    return None


@app.get("/authors/{author_id}/books", response_model=list[schemas.BookOut])
def read_author_books(author_id: int, db: Session = Depends(get_db)):
    author = crud.get_author(db, author_id)
    if author is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Author not found")
    return author.books
