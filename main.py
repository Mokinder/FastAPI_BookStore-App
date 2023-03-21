from fastapi import FastAPI,HTTPException
import os
import json
from Model.Book import Book
from uuid import uuid4
from fastapi.encoders import jsonable_encoder

app = FastAPI()

Books_File="books.json"

Book_Database = [
    "The Great Alexander",
    "The History of Hitler",
    "The Impact of World War I,II"
]

if os.path.exists(Books_File):
    with open(Books_File,"r") as f:
        Book_Database = json.load(f)


@app.get("/bookstore/home")
async def home():
    return {"Welcome to Book_Store Home_Page!!"}

@app.get("/bookstore/list-books")
async def list_books():
    return {"Books": Book_Database}

@app.get(f"/bookstore/get_id/{id}")
async def get_id( id : int):
    if id<0 or id >= len(Book_Database):
        raise HTTPException(404,"Not Found")
    else :
        return {"Books": Book_Database[id]}


@app.post("/bookstore/add-book")
async def add_book(book : Book):
    book.book_id=uuid4().int
    json_book = jsonable_encoder(book)
    Book_Database.append(json_book)
    with open(Books_File, "w") as f:
        json.dump(Book_Database,f)
    if Book_Database[len(Book_Database)-1] == book :
            return f"ID : {book.book_id}, Name : {book.name} is added successfully!!"
    else :
            return HTTPException(404,"Something went wrong try again!!")

