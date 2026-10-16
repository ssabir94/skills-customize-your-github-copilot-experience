from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel


class BookInput(BaseModel):
    title: str
    author: str


class Book(BookInput):
    id: int


app = FastAPI()

books: dict[int, Book] = {
    1: Book(id=1, title="The Hobbit", author="J.R.R. Tolkien"),
    2: Book(id=2, title="A Wrinkle in Time", author="Madeleine L'Engle"),
}


@app.get("/books", response_model=list[Book])
def list_books():
    # TODO: Return all books.
    pass


@app.get("/books/{book_id}", response_model=Book)
def get_book(book_id: int):
    # TODO: Return the requested book, or raise HTTPException with status 404.
    pass


@app.post("/books", response_model=Book, status_code=status.HTTP_201_CREATED)
def create_book(book_input: BookInput):
    # TODO: Assign an unused integer ID, save the book, and return it.
    pass


@app.put("/books/{book_id}", response_model=Book)
def update_book(book_id: int, book_input: BookInput):
    # TODO: Replace the existing book's title and author, or raise HTTPException with status 404.
    pass


@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    # TODO: Delete the book, or raise HTTPException with status 404.
    # On success, return a JSON confirmation message.
    pass
