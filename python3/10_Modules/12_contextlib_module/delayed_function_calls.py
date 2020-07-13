#!/usr/bin/python
"""
Purpose: Go defer-like delayed calls

"""
import contextlib


def callback():
    print('B')


with contextlib.ExitStack() as stack:
    stack.callback(callback)
    print('A')
