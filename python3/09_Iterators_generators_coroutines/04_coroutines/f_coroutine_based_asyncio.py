import asyncio


@asyncio.coroutine
def old_style_coroutine():
    print('old_style_coroutine - start')
    yield from asyncio.sleep(1)
    print('old_style_coroutine - end')


async def main():
    print('main - start')
    await old_style_coroutine()
    print('main - end')

asyncio.run(main())


# NOTE: To ignore warnings when running a script,
# python -W ignore script_name.py
# or export PYTHONWARNINGS="ignore"
