import asyncio
import time
import random
from concurrent.futures import ThreadPoolExecutor

owner = None

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

async def sleep(executor=None):
    loop = asyncio.get_event_loop()
    await loop.run_in_executor(executor, time.sleep, 1)

async def main():
    executor = ThreadPoolExecutor(max_workers=100)
    futures = [asyncio.ensure_future(sleep(executor)) for i in range(100)]
    await asyncio.gather(*futures)

async def coro1(lock):
    global owner

    await lock.acquire()
    owner = "IAMMAN"
    print(f"I am owner, {owner}")
    await asyncio.sleep(random.random())
    print(f"{owner} is man.")
    lock.release()

async def coro2(lock):
    global owner

    async with lock:
        owner = "IAMWOMAN"
        print(f"I am owner, {owner}")
        await asyncio.sleep(random.random())
        print(f"{owner} is woman.")


async def switching():
    lock = asyncio.Lock()

    while True:
        await asyncio.gather(coro1(lock), coro2(lock))
        await asyncio.sleep(0.1)


if __name__ == "__main__":
    start = time.time()
    # loop = asyncio.get_event_loop()
    # Specify scheduling order by asyncio.gather
    # loop.run_until_complete(asyncio.gather(coroutine_1(), coroutine_2(), coroutine_3(), hello(10, 20)))
    # loop.close()
    asyncio.run(main())
    print(f"taken: {time.time() - start}")

    asyncio.run(switching())
