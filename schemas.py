from typing import Optional
from pydantic import BaseModel, ConfigDict

# AUTHOR

class AuthorBase(BaseModel):
    name: str


class AuthorCreate(AuthorBase):
    pass


class AuthorOut(AuthorBase):
    id: int
    model_config = ConfigDict(from_attributes=True)


# BOOK

class BookBase(BaseModel):
    title: str
    genre: Optional[str] = None
    year_publication: Optional[int] = None


class BookCreate(BookBase):
    author_id: Optional[int] = None


class BookOut(BookBase):
    id: int
    author_id: Optional[int] = None
    model_config = ConfigDict(from_attributes=True)


class AuthorWithBooks(AuthorOut):
    books: list[BookOut] = []
