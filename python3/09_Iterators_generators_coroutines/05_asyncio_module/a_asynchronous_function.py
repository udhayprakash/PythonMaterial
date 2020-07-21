# /usr/bin/python
"""
Purpose: asyncio
    working from python 3.7+
    In Python 3.7, two new keywords (async and await) were introduced
"""

import asyncio

def hello():
    print('Hello')
    print('world')

hello()


async def asynchronous_hello():
    print('Hello')
    print('World')

# asynchronous_hello()
# a_asyncio_ex.py:21: RuntimeWarning: coroutine 'asynchronous_hello' was never awaited

print()
loop = asyncio.get_event_loop()
loop.run_until_complete(asynchronous_hello())
loop.close() 

print()
asyncio.run(asynchronous_hello())