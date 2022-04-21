#!/usr/bin/python
"""
Purpose: asyncio
    asyncio.wait: wait for a sequence of awaitables,
       until the given ‘condition’ is met.

FIRST_COMPLETED     The function will return when any future finishes or is cancelled.
FIRST_EXCEPTION     The function will return when any future finishes by raising an exception.
                    If no future raises an exception then it is equivalent to ALL_COMPLETED.
ALL_COMPLETED       The function will return when all futures finish or are cancelled.
"""
import asyncio
from random import randrange


async def foo(n):
    s = randrange(5)
    print(f"{n} will sleep for: {s} seconds")
    await asyncio.sleep(s)
    print(f"n: {n}!")


async def main():
    tasks = [foo(1), foo(2), foo(3)]
    result = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)
    print(result)


# NOTE: FIRST_COMPLETED option, meaning whichever
# task finishes first is what will be returned.

asyncio.run(main())
