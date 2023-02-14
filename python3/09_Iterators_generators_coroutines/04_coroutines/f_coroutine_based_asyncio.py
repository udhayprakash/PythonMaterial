#!/usr/bin/python3
"""
Purpose: asyncio
"""
import asyncio

# print(dir(asyncio))

# blocking execution- traditional - pytho.java,c, c++
# statement1 - 5sec
# statement1 - 5sec
# statement1 - 5sec
# 5 + 5 + 5 = 15 sec

# non-blocking execution- node.js. asyncio
# statement1 - 5sec
# statement1 - 5sec
# statement1 - 5sec
# 5 sec


@asyncio.coroutine
def old_style_coroutine():
    print("old_style_coroutine - start")
    yield from asyncio.sleep(1)
    print("old_style_coroutine - end")


# osc = old_style_coroutine()
# print(f'{osc = }')
# print(f'{list(osc) = }')

asyncio.run(old_style_coroutine())
print()


# --------------------------------
# async, await -- new keywords in python 3.7
async def main():
    print("main - start")
    await old_style_coroutine()
    print("main - end")


asyncio.run(main())


# NOTE: To ignore warnings when running a script,
# python -W ignore script_name.py
# or export PYTHONWARNINGS="ignore"
