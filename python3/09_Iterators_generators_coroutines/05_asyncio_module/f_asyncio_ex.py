#!/usr/bin/python3
"""
Purpose: asyncio
    asynchrnous functions should be called with await,
    even within another asynchronous functions
"""
import asyncio


async def nested():
    return 42


async def main():
    # Nothing happens if we just call "nested()".
    # A coroutine object is created but not awaited,
    # so it *won't run at all*.

    # nested()  # RuntimeWarning: coroutine 'nested' was never awaited

    # Let's do it differently now and await it:
    print(await nested())  # will print "42".

    result = await nested()
    print(f"{result =}")


asyncio.run(main())


# NOTE: RuntimeWarning cant be handled with exceptions
