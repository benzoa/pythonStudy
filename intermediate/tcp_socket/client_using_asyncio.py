import asyncio


async def start_client(message: str):
    reader: asyncio.StreamReader
    writer: asyncio.StreamWriter

    reader, writer = await asyncio.open_connection('127.0.0.1', 5577)
    print('[C]Connected')
    writer.write(message.encode())
    await writer.drain()
    print(f'[C]Send: {message!r}')

    data = await reader.read(100)
    print(f'[C]Received: {data.decode()!r}')

    print('[C]Closing...')
    writer.close()
    await writer.wait_closed()

