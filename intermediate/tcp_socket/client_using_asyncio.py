import asyncio
from random import random

_port = 7770

async def run_client(host: str, port: int):
    reader: asyncio.StreamReader
    writer: asyncio.StreamWriter
    reader, writer = await asyncio.open_connection(host, port)

    # show connection info
    print("[C] connected")

    while True:
        line = input("[C] enter message: ")
        if not line:
            break

        payload = line.encode()
        writer.write(payload)
        await writer.drain()
        print(f"[C] sent: {len(payload)} bytes.\n")

        data = await reader.read(1024)  # type: bytes
        print(f"[C] received: {len(data)} bytes")
        print(f"[C] message: {data.decode()}")

    print("[C] closing connection...")
    writer.close()
    await writer.wait_closed()


async def main():
    await asyncio.wait(run_client("127.0.0.1", _port))


if __name__ == "__main__":
    asyncio.run(main())
