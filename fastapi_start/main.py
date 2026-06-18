import router_example

from fastapi import FastAPI

app = FastAPI()

app.include_router(router_example.router)

# This instance houses the code of your application.


# Routes 
@app.get("/")
async def read_root():
    return {"Hello" : "World"}


