#!/usr/bin/python3
"""
Purpose:
"""
import asyncio
import time


async def myWorker(semaphore):
    await semaphore.acquire()
    print("Successfully acquired the semaphore")
    await asyncio.sleep(3)
    print("Releasing Semaphore")
    semaphore.release()


async def main(loop):
    mySemaphore = asyncio.Semaphore(value=2)
    await asyncio.wait(
        [myWorker(mySemaphore), myWorker(mySemaphore), myWorker(mySemaphore)]
    )
    print("Main Coroutine")


loop = asyncio.get_event_loop()
loop.run_until_complete(main(loop))
print("All Workers Completed")
loop.close()
