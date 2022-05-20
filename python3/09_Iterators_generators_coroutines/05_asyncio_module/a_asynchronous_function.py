# /usr/bin/python3
"""
Purpose: asyncio
    working from python 3.7+
    In Python 3.7, two new keywords (async and await) were introduced


Python/java/c++
    statement 1 - 5s
    statement 2 - 5s
    statement 3 - 5s
    ----------------
        total - 15s - Blocking Execution - one after another

Node.js/ python-asyncio / Goroutines
    statement 1 - 5s
    statement 2 - 5s
    statement 3 - 5s
    ----------------
        total - 5s - non-Blocking Execution

"""
import asyncio


def hello():
    print("Hello")
    print("world")


hello()


async def asynchronous_hello():
    print("Hello")
    print("World")


# asynchronous_hello()
# RuntimeWarning: coroutine 'asynchronous_hello' was never awaited
#   asynchronous_hello()
# RuntimeWarning: Enable tracemalloc to get the object allocation traceback


print()
# Method 1
loop = asyncio.get_event_loop()  # DeprecationWarning: There is no current event loop
loop.run_until_complete(asynchronous_hello())
loop.close()


# Method 2
print()
asyncio.run(asynchronous_hello())
