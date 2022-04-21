#!/usr/bin/python
"""
Purpose: Exceptions in atexit Callbacks

"""
import atexit


def exit_with_exception(message):
    raise RuntimeError(message)


atexit.register(exit_with_exception, "Registered first")
atexit.register(exit_with_exception, "Registered second")
