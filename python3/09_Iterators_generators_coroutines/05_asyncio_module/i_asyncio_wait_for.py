#!/usr/bin/python3
"""
Purpose: asyncio
    asyncio.wait_for: wait for a single awaitable,
        until the given ‘timeout’ is reached.
"""
import asyncio


async def foo(n):
    await asyncio.sleep(4)
    # await asyncio.sleep(7)
    print(f"n: {n}!")


async def main():
    try:
        await asyncio.wait_for(foo(1), timeout=5)
    except asyncio.TimeoutError as ex:
        print(ex)  # no error message comes from this exception
        print("timeout!")


asyncio.run(main())
