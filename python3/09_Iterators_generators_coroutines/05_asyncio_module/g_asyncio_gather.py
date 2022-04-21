#!/usr/bin/python3
"""
Purpose: asyncio
    asyncio.gather: takes a sequence of awaitables,
        returns an aggregate list of successfully awaited values.
"""
import asyncio


async def foo(n):
    # await asyncio.sleep(3)  # wait 3s before continuing
    await asyncio.sleep(n)  # wait ns before continuing
    print(f"n: {n}!")


async def main():
    # tasks = [foo(1), foo(2), foo(3)]
    tasks = [foo(3), foo(2), foo(1)]
    await asyncio.gather(*tasks)


asyncio.run(main())

"""
1s -
2s --
3s ---

3s ---
2s --
1s -


"""
