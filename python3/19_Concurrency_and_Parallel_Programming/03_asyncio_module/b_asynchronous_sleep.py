# /usr/bin/python
"""
Purpose: asyncio
    working from python 3.7+
    In Python 3.7, two new keywords (async and await) were introduced

NOTE:
    If you lock coroutine synchronously — maybe you use time.sleep(10)
    instead of await asyncio.sleep(10) — you do not return control to
    the event loop — the whole process will be blocked.
"""
import asyncio
import time


def hello():
    print("Hello")
    time.sleep(2)
    print("world")


hello()


async def asynchronous_hello():
    print("Hello")
    # time.sleep(2)
    await asyncio.sleep(2)
    print("World")


# asynchronous_hello()
# RuntimeWarning: coroutine 'asynchronous_hello' was never awaited

print()
asyncio.run(asynchronous_hello())

print("Next statement")

# stat1 - 2s
# stat2 - 1s
# stat3 - 2s
# stat4 - 2s
# ----------
# total - 7s  - blocking code - python
# total - 2s  - non-blocking code - python-asyncio
