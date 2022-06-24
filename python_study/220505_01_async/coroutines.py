
import asyncio



async def main():
    print("coroutines!")
    # introducing the concept of task
    task = asyncio.create_task(foo("hello from foo"))
    await task
    print(type(task))
    print(task)
    print("Finished")

async def foo(text):
    print(text)
    await asyncio.sleep(1)

# await main()
asyncio.run(main())


# asyn event loop

