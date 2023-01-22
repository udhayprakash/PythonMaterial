#!/usr/bin/python
"""
Purpose: partialmethod()
    - function, which returns partialmethod descriptors.
    - You can think of it as the partial() function for methods.
    - This means, it is not intended to be callable, but as a way
      to define new methods.
"""

from functools import partialmethod


class Cell(object):
    def __init__(self):
        self._alive = False

    @property
    def alive(self):
        return self._alive

    def set_state(self, state):
        self._alive = bool(state)

    set_alive = partialmethod(set_state, True)
    set_dead = partialmethod(set_state, False)


c = Cell()
c.set_alive()
print(c.alive)
