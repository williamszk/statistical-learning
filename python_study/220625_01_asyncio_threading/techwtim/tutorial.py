
import asyncio
from re import I

async def foo():
    print("Bananas")
    task = asyncio.create_task(spam("Hi from spam"))
    await asyncio.sleep(1)
    print("1 Finished") 
    print("2 Finished") 
    print("3 Finished") 
    await task

# print(type(foo()))
# <class 'coroutine'>

# async event-loop
async def spam(text):
    # the await will execute the coroutine
    print(text)
    await asyncio.sleep(10)
    # print("Finished the spam function")
    with open("message_spam.txt", "w") as f:
        f.write("Hi there")
    


asyncio.run(foo())