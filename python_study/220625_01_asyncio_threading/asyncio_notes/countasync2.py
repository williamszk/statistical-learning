# use create_task instead of gather but make the same result
import asyncio


async def count():
    print("Start")
    await asyncio.sleep(1)
    print("Finish")


async def main():
    task1 = asyncio.create_task(count())
    task2 = asyncio.create_task(count())
    task3 = asyncio.create_task(count())

    await task1
    await task2
    await task3


if __name__ == "__main__":
    import time
    s = time.perf_counter()
    asyncio.run(main())
    elapsed = time.perf_counter() - s
    print(f"{__file__} executed in: {elapsed:0.2f} seconds")
