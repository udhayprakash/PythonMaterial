#!/usr/bin/python
"""
Purpose: asyncio
    asyncio.as_completed: similar to gather but returns
        Futures that are populated when results are ready.

    Takes many awaitables in an iterable.
    Yields Futures that you have to await as soon as something is done.
    Does not guarantee to return the original awaitables that you passed in.
    Does wrap the awaitables in tasks (it actually calls asyncio.ensure_future() on them).
    Takes an optional timeout.
"""
import asyncio
from random import randrange


async def foo(n):
    s = randrange(10)
    print(f"{n} will sleep for: {s} seconds")
    await asyncio.sleep(s)
    return f"{n}!"


async def main():
    counter = 0
    tasks = [foo("a"), foo("b"), foo("c")]

    for future in asyncio.as_completed(tasks):
        n = "quickest" if counter == 0 else "next quickest"
        counter += 1
        result = await future
        print(f"the {n} result was: {result}")


asyncio.run(main())
