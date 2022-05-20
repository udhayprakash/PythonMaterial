# /usr/bin/python3
"""
Purpose: asyncio
    working from python 3.7+
"""
import asyncio
import time


async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)


async def main():
    print(f"started at {time.strftime('%X')}")

    await say_after(4, "hello")  # 4s
    await say_after(2, "world")  #  2s

    print(f"finished at {time.strftime('%X')}")


asyncio.run(main())
