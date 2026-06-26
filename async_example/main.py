#1. FastAPI Server 
from fastapi import FastAPI
app = FastAPI()

# 2. Create an endpoint that sleep for 1 second
import time 
@app.get("/sync")
def read_sync():
    time.sleep(2)
    return{
        "message":"Synchrounous blocking endpoint"
    }

# 3. Now create same endpoint for the async def
import asyncio
@app.get("/async")
async def read_async():
    await asyncio.sleep(2)
    return{
        "message":"Asynchronous non-blocking endpoint"
    }


