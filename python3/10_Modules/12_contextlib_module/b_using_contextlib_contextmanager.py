#!/usr/bin/python
"""
Purpose:

"""
from contextlib import contextmanager


@contextmanager
def ctx():
    print("\nstart")
    yield
    print("end")


c = ctx()
with c:
    print("\tmiddle")

with ctx() as c:
    print("\tmiddle")
