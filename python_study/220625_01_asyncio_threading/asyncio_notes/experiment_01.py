import asyncio

async def f():
    print("Runnin long process inside f function")
    asyncio.sleep(5)
    return None

async def g():
    print("Runnin long process inside g function")
    await f()
    asyncio.sleep(3)
    return None


async def main():
    await g()
    return None

if __name__ == "__main__":
    main()

