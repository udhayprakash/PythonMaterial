#!/usr/bin/python3
"""
Purpose: Understanding asyncio event loop

"""
import asyncio
import time


def ordinary_say_after(delay, message):
    time.sleep(delay)
    print(message)


async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)
    return "something"


def hello_world1():
    ordinary_say_after(2, "Golang")

    # say_after(2, "Golang")
    # await say_after(2, "Golang")
    asyncio.run(say_after(2, "Golang"))  # ONLY ONE EVENT LOOP possible


hello_world1()


async def hello_world2():
    ordinary_say_after(2, "Golang")

    # say_after(2, "Golang")
    await say_after(2, "Golang")
    # asyncio.run(say_after(2, "Golang")) # ONLY ONE EVENT LOOP possible

    task = asyncio.create_task(say_after(2, "Hello"))


asyncio.run(hello_world2())
asyncio.run(hello_world2())
