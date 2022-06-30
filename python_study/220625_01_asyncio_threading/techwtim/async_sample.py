import asyncio
import time
async def fetch_data():
    print("start fetching")
    await asyncio.sleep(2)
    print("done fetching")
    return {"data": 1}

async def print_numbers():
    for i in range(10):
        print(i)
        await asyncio.sleep(0.3)


async def main():
    s = time.perf_counter()
    task1 = asyncio.create_task(fetch_data())
    # print(type(task1))
    task2 = asyncio.create_task(print_numbers())

    value = await task1
    print(value)
    await task2
    print(f"elapsed time: {time.perf_counter() - s}")

asyncio.run(main())

