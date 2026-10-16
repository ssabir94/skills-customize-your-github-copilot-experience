# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a REST API with FastAPI that lets clients manage a small collection of books. Practice HTTP methods, URL paths, JSON request and response data, and handling missing resources.

## 📝 Tasks

### 🛠️ Create the API and Read Books

#### Description
Use the provided `main.py` starter file to create a FastAPI application for the in-memory books collection. Install FastAPI and Uvicorn with `python -m pip install fastapi uvicorn`, then run the app from the assignment folder with `uvicorn main:app --reload`.

#### Requirements
Completed program should:

- Create a FastAPI application that can be opened at `http://127.0.0.1:8000`.
- Implement `GET /books` to return all books as JSON.
- Implement `GET /books/{book_id}` to return one matching book.
- Return HTTP 404 when a requested book ID does not exist.
- Use the interactive API documentation at `http://127.0.0.1:8000/docs` to try both GET routes.

### 🛠️ Add and Update Books

#### Description
Add endpoints that let clients create a book and replace the details of an existing book by sending JSON request bodies.

#### Requirements
Completed program should:

- Use the provided Pydantic `BookInput` model to validate a book's title and author.
- Implement `POST /books` to add a book, assign it a unique integer ID, and return the new book.
- Return HTTP 201 when a book is created.
- Implement `PUT /books/{book_id}` to replace the title and author of an existing book.
- Return HTTP 404 when a client tries to update a book ID that does not exist.

### 🛠️ Delete Books and Check API Behavior

#### Description
Complete the API by allowing clients to delete a book. Use the interactive documentation to test successful requests and expected errors.

#### Requirements
Completed program should:

- Implement `DELETE /books/{book_id}` to remove the specified book.
- Return a JSON confirmation message after a successful deletion.
- Return HTTP 404 when a client tries to delete a book ID that does not exist.
- Verify in `/docs` that create, read, update, and delete requests work and that missing IDs produce 404 responses.
