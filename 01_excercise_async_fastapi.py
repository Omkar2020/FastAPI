from fastapi import FastAPI
import asyncio
from typing import List


app = FastAPI()

@app.get("/countdown", response_model=List[int])
async def countdown() -> List[int]:
    numbers = []
    for i in range(101):
        await asyncio.sleep(0.01)   
        numbers.append(i)
    return numbers