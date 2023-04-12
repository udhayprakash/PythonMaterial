import asyncio
import inspect


def plain_old_function():
    return "Plain old function"


async def async_function():
    return "Async function"


async def await_me_maybe(callback):
    result = callback()
    if inspect.isawaitable(result):
        return await result
    return result


async def run_framework():
    print(await await_me_maybe(plain_old_function))
    print(await await_me_maybe(async_function))


if __name__ == "__main__":
    asyncio.run(run_framework())
