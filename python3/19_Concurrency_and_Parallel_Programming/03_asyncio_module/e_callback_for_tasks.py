#!/usr/bin/python3
"""
Purpose: asyncio
"""
import asyncio


async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)
    return "something"


def got_result(future):
    # print(f'{type(future) = }')
    # print(f'{dir(future)  = }')
    print(f"got the result! {future.result()}")


async def hello_world():
    task = asyncio.create_task(say_after(2, "Hello"))
    task.add_done_callback(got_result)
    print(task)

    await asyncio.sleep(5)
    print("Hello World!")

    await asyncio.sleep(10)
    print(task)


asyncio.run(hello_world())


# NOTE:
# 1. More than one callback can be added to a task
# 2. task.remove_done_callback() to remove a
#    callback from the callbacks list.
