import asyncio
import random
from concurrent.futures import ThreadPoolExecutor
from time import sleep


def return_after_5_secs(message):
    sleep(5)
    return message


pool = ThreadPoolExecutor(3)


async def doit():
    identify = random.randint(1, 100)
    future = pool.submit(return_after_5_secs, (f'result: {identify}'))
    awaitable = asyncio.wrap_future(future)
    print(f'waiting result: {identify}')
    return await awaitable


async def app():
    # run some stuff multiple times
    tasks = [doit(), doit()]

    result = await asyncio.gather(*tasks)
    print(result)

print('waiting app')
asyncio.run(app())
