from sqlalchemy.orm import Session
import models
import schemas

# BOOKS

def get_books(db: Session):
    return db.query(models.Book).all()


def get_book(db: Session, book_id: int):
    return db.query(models.Book).filter(models.Book.id == book_id).first()


def create_book(db: Session, book: schemas.BookCreate):
    db_book = models.Book(**book.model_dump())
    db.add(db_book)
    db.commit()
    db.refresh(db_book)  
    return db_book


def update_book(db: Session, book_id: int, book: schemas.BookCreate):
    db_book = get_book(db, book_id)
    if db_book is None:
        return None
    for field, value in book.model_dump().items():
        setattr(db_book, field, value)
    db.commit()
    db.refresh(db_book)
    return db_book


def delete_book(db: Session, book_id: int):
    db_book = get_book(db, book_id)
    if db_book is None:
        return None
    db.delete(db_book)
    db.commit()
    return db_book


# AUTHORS

def get_authors(db: Session):
    return db.query(models.Author).all()


def get_author(db: Session, author_id: int):
    return db.query(models.Author).filter(models.Author.id == author_id).first()


def create_author(db: Session, author: schemas.AuthorCreate):
    db_author = models.Author(**author.model_dump())
    db.add(db_author)
    db.commit()
    db.refresh(db_author)
    return db_author


def update_author(db: Session, author_id: int, author: schemas.AuthorCreate):
    db_author = get_author(db, author_id)
    if db_author is None:
        return None
    for field, value in author.model_dump().items():
        setattr(db_author, field, value)
    db.commit()
    db.refresh(db_author)
    return db_author


def delete_author(db: Session, author_id: int):
    db_author = get_author(db, author_id)
    if db_author is None:
        return None
    db.delete(db_author)
    db.commit()
    return db_author
