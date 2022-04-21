#!/usr/bin/python
"""
Purpose: cancelling a run task
    asyncio.cancel - Request the Task to be cancelled.

"""
import asyncio

async def cancel_me():
    print('cancel_me(): before sleep')

    try:
        # Wait for 1 hour
        await asyncio.sleep(3600)
    except asyncio.CancelledError:
        print('cancel_me(): cancel sleep')
        raise
    finally:
        print('cancel_me(): after sleep')

async def main():
    # Create a "cancel_me" Task
    task = asyncio.create_task(cancel_me())

    # Wait for 1 second
    await asyncio.sleep(1)

    print(f'main(): Before cancelling: {task.cancelled()=}') # False
    task.cancel()
    print(f'main(): After  cancelling: {task.cancelled()=}') # False

    try:
        await task
    except asyncio.CancelledError:
        print('main(): cancel_me is cancelled now')
        print(f'{task.exception =}')

    print(f'main(): After  cancelling: {task.cancelled()=}') # True

asyncio.run(main())

# cancel_me(): before sleep
# cancel_me(): cancel sleep
# cancel_me(): after sleep
# main(): cancel_me is cancelled now
