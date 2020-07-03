#!/usr/bin/python
"""
Purpose: atexit 
    – Call functions when a program is closing down
    The callbacks registered with atexit are not invoked if:
        - the program dies because of a signal
        - os._exit() is invoked directly
        - a Python fatal error is detected (in the interpreter)
"""
import atexit


def my_cleanup(name):
    print('my_cleanup(%s)' % name)


atexit.register(my_cleanup, 'first')
atexit.register(my_cleanup, 'second')
atexit.register(my_cleanup, 'third')

# raise Exception()