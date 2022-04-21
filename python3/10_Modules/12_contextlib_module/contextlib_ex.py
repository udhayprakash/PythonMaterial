#!/usr/bin/python
"""
Purpose:

"""
from contextlib import contextmanager


@contextmanager
def ctx():
    print("start")
    yield
    print("end")


c = ctx()
with c:
    print("middle")

with ctx() as c:
    print("middle")
