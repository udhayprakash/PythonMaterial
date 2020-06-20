#!/usr/bin/python
"""
Purpose: Pools
    When dealing with lots of concurrent operations 
    it might be wise to utilize a ‘pool’ of threads 
    (and/or subprocesses) to prevent exhausting your 
    application’s host resources.

    concurrent.futures has "Executors" to help for this.
        1. ThreadPoolExecutor (default for asyncio.run_in_executor)
        2. ProcessPoolExecutor
"""
import os 
import sys
import asyncio
import concurrent.futures


def blocking_io():
    # File operations (such as logging) can block the
    # event loop: run them in a thread pool.
    python_license = os.path.join(sys.exec_prefix, 'LICENSE.txt')
    with open(python_license, "rb") as f:
        return f.read(50)


def cpu_bound():
    # CPU-bound operations will block the event loop:
    # in general it is preferable to run them in a
    # process pool.
    return sum(i * i for i in range(10 ** 7))


async def main():
    loop = asyncio.get_running_loop()

    # 1. Run in the default loop's executor:
    result = await loop.run_in_executor(None, blocking_io)
    print("default thread pool", result)

    # 2. Run in a custom thread pool:
    with concurrent.futures.ThreadPoolExecutor() as pool:
        result = await loop.run_in_executor(pool, blocking_io)
        print("custom thread pool", result)

    # 3. Run in a custom process pool:
    with concurrent.futures.ProcessPoolExecutor() as pool:
        result = await loop.run_in_executor(pool, cpu_bound)
        print("custom process pool", result)


asyncio.run(main())