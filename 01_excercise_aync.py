import asyncio

async def countdown() -> list [int]:
    numbers = []
    for i in range (101):
        await asyncio.sleep(0.01)
        numbers.append(i)
    return numbers
    
    
if __name__=="__main__":
    result = asyncio.run(countdown())
print (result)