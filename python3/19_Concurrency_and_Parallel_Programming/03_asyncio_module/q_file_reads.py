import asyncio

import nest_asyncio
from aiofile import async_open

# pip install nest_asyncio


async def main():
    async with async_open("/tmp/hello.txt", "w+") as afp:
        await afp.write("Hello ")
        await afp.write("world ")
        afp.seek(0)
        # breakpoint()
        print(await afp.read())
