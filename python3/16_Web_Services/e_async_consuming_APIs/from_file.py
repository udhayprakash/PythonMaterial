import asyncio

import aiohttp


async def read_data_from_file(filename):
    async with aiohttp.ClientSession() as session:
        async with session.get(f"file://{filename}") as response:
            data = await response.text()
            return data


async def main():
    filename = "example.txt"
    data = await read_data_from_file(filename)
    print(data)


if __name__ == "__main__":
    asyncio.run(main())
