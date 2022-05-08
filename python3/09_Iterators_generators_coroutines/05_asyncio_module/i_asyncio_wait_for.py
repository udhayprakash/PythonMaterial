#!/usr/bin/python3
"""
Purpose: asyncio
    asyncio.wait_for: wait for a single awaitable,
        until the given "timeout" is reached.

    Takes one awaitable.
    Wraps the awaitable in a task if necessary.
    Takes a timeout that cancels the task if it expires.
    Unlike create_task(), is a coroutine itself that doesn't execute until awaited.
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
