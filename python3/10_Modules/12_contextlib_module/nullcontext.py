import contextlib

with contextlib.nullcontext():
    print('Nothing special')     # Nothing special

# with optional argument
with contextlib.nullcontext('world') as planet:
    print('Hello', planet)  # Hello world
