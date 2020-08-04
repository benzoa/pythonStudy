import asyncio

async def add(a, b):
    return a + b

async def hello(a, b):
    print("Hello World")
    ret = await add(a, b)
    print("{} + {} = {}".format(a, b, ret))

loop = asyncio.get_event_loop()
loop.run_until_complete(hello(10, 20))
loop.close()
