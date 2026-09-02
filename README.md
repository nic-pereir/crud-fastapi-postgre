# Book API — Library CRUD (FastAPI + SQLAlchemy + Pydantic)

A small REST API built with **FastAPI**, **SQLAlchemy** and **Pydantic**, implementing a full CRUD for a library system (books and authors, with a one-to-many relationship between them).

This project was built as a study/reference example while learning backend development — it favors clarity over completeness, so each file has a single, well-defined responsibility.

## Features

- Full CRUD for `Book` and `Author` resources
- One-to-many relationship (`Author` → `Book`) via SQLAlchemy's `relationship()`
- Request validation and response formatting with Pydantic schemas
- Proper HTTP status codes (`201 Created`, `204 No Content`, `404 Not Found`)
- Interactive API docs via Swagger UI
- `GET /authors/{id}/books` — nested resource endpoint, no manual JOIN needed
- A standalone `exemplo_01_crud_memoria.py` showing the same CRUD logic without a database, as a stepping stone

## Tech stack

- [FastAPI](https://fastapi.tiangolo.com/)
- [SQLAlchemy](https://www.sqlalchemy.org/) (ORM)
- [Pydantic](https://docs.pydantic.dev/)
- SQLite by default (zero setup), swappable for PostgreSQL/MySQL via `DATABASE_URL`

## Project structure

```
.
├── main.py       # FastAPI app and HTTP routes
├── database.py   # Engine, session, and DB connection setup
├── models.py     # SQLAlchemy ORM models (tables)
├── schemas.py    # Pydantic schemas (request/response validation)
└── crud.py       # Database access functions (SELECT/INSERT/UPDATE/DELETE)
```

## Getting started

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

Then open `http://127.0.0.1:8000/docs` for the interactive Swagger UI.

By default the API uses SQLite (a `livraria.db` file created automatically on first run). To use PostgreSQL or MySQL instead, set the `DATABASE_URL` environment variable, e.g.:

```bash
export DATABASE_URL="postgresql://user:password@localhost:5432/dbname"
```

## Endpoints

| Method | Endpoint                | Description                     |
|--------|--------------------------|----------------------------------|
| GET    | `/books`                | List all books                  |
| GET    | `/books/{id}`            | Get a single book               |
| POST   | `/books`                 | Create a new book                |
| PUT    | `/books/{id}`            | Update a book                    |
| DELETE | `/books/{id}`            | Delete a book                    |
| GET    | `/authors`               | List all authors                 |
| GET    | `/authors/{id}`          | Get a single author              |
| POST   | `/authors`                | Create a new author              |
| PUT    | `/authors/{id}`          | Update an author                 |
| DELETE | `/authors/{id}`          | Delete an author                 |
| GET    | `/authors/{id}/books`    | List all books by a given author |

---
Developed by Nicolly Pereira