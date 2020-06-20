#!/usr/bin/python
"""
Purpose: asyncio tasks
"""
import asyncio
import time
from pprint import pprint


async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)


async def main():
    # # case 1 - first task takes less time compared to seccond one
    # task1 = asyncio.create_task(say_after(1, 'hello'))
    # task2 = asyncio.create_task(say_after(2, 'world'))

    # case 2 - first task takes MORE time compared to seccond one
    task1 = asyncio.create_task(say_after(4, 'hello'))
    task2 = asyncio.create_task(say_after(2, 'world'), name='print_world')

    print(f"started at {time.strftime('%X')}")

    # Wait until both tasks are completed (should take
    # around 2 seconds.)
    await task1
    await task2

    print(f"finished at {time.strftime('%X')}")

    print(f'\n{task1.get_name()=}')
    print(f'{task2.get_name()=}')
    print(f'{task1.done()      =}')
    print(f'{task2.done()      =}')

    pprint(asyncio.all_tasks())
    print(len(asyncio.all_tasks()))

asyncio.run(main())
