#  main.py file containing the server instance:
from fastapi import FastAPI, HTTPException
from models import Book
from pydantic import BaseModel 
from starlette.responses import JSONResponse



app = FastAPI()
# @app.get("/books/{book_id}")
# async def read_book(book_id:int):
#     return{
#         "book_id":book_id,
#         "title":"The Great India",
#         "author":"MK Ji"
#     }

class BookResponse(BaseModel):
   title:str
   author:str

@app.get("/allbooks")
async def read_all_books() -> list[BookResponse]:
   return [
      {
         "id":1,
         "title":"2026",
         "author":"Op kumar"
      },
       {
         "id":1,
         "title":"The Great India",
         "author":"HC verma"
      },

   ]
@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
   return JSONResponse(
      status_code=exc.status_code,
      content={
         "message":"Ops! Something went wrong"
      }
   )

@app.get("/error_endpoint")
async def raise_exception():
   raise HTTPException(status_code=400)


@app.post("/book")
async def create_book(book:Book):
   return book

@app.get("/books")
async def read_book(year:int=None):
    if year:
     return{
        "year":year,
        "books":["Book 1", "Book 2"]
    }
    return {"books":["All Books"]}

@app.get("/authors/{author_id}")
async def read_author(author_id:int):
    return{
        "author_id":author_id,
        "name":"Ernest Heminway"
    }

# 53 
