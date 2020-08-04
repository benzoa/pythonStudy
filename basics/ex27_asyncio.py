import asyncio
import time

async def add(a, b):
    await asyncio.sleep(1.0)
    return a + b

async def hello(a, b):
    print("Hello World")
    ret = await add(a, b)
    print("{} + {} = {}".format(a, b, ret))

async def coroutine_1():
    print("Start coroutine 1")
    await asyncio.sleep(3.0)
    print("Resume coroutine 1")

async def coroutine_2():
    print("Start coroutine 2")
    await asyncio.sleep(2.0)
    print("Resume coroutine 2")

async def coroutine_3():
    print("Start coroutine 3")
    loop = asyncio.get_event_loop()
    # to make as subroutine act like a coroutine with threading
    loop.run_in_executor(None, time.sleep, 1)
    print("Resume coroutine 3")

if __name__ == "__main__":
    loop = asyncio.get_event_loop()

    start = time.time()
    # Specify scheduling order by asyncio.gather
    loop.run_until_complete(asyncio.gather(coroutine_1(), coroutine_2(), coroutine_3(), hello(10, 20)))
    print(f"taken: {time.time() - start}")
    loop.close()
