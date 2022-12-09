# https://www.youtube.com/watch?v=6RbJYN7SoRs&ab_channel=NeuralNine
import asyncio

async def main():
    task = asyncio.create_task(other_function())
    print("A")
    await asyncio.sleep(5)
    print("B")
    out_create = await task
    print(f"{out_create = }")

async def other_function():
    print("1")
    await asyncio.sleep(2)
    print("2")
    return 10

if __name__ == "__main__":
    asyncio.run(main()) 