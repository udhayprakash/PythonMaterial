#!/usr/bin/python
"""
Purpose: sched module
"""

import time

try:
    import sched
except ImportError:
    from os import system

    system('python -m pip install sched')
    import sched

scheduler = sched.scheduler(time.time, time.sleep)


def print_event(name):
    print('EVENT:', time.time(), name)


print('START:', time.time())
scheduler.enter(2, 1, print_event, ('first',))
scheduler.enter(3, 1, print_event, ('second',))

scheduler.run()
