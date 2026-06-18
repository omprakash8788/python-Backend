#  main.py file containing the server instance:
from fastapi import FastAPI

app = FastAPI()
# @app.get("/books/{book_id}")
# async def read_book(book_id:int):
#     return{
#         "book_id":book_id,
#         "title":"The Great India",
#         "author":"MK Ji"
#     }

@app.get("/books")
async def read_book(year:int=None):
    if year:
     return{
        "year":year,
        "books":["Book 1", "Book 2"]
    }

@app.get("/authors/{author_id}")
async def read_author(author_id:int):
    return{
        "author_id":author_id,
        "name":"Ernest Heminway"
    }