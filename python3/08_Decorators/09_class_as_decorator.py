#!/usr/bin/python
"""
Purpose: Class as decorator
    As of PEP 3129, starting in Python 3, decorators
can also be applied to classes.
"""


class bol(object):
    def __init__(self, f):
        self.f = f

    def __call__(self):
        return "<b>{}</b>".format(self.f())


class ita(object):
    def __init__(self, f):
        self.f = f

    def __call__(self):
        return "<i>{}</i>".format(self.f())


@bol
@ita
def sayhi():
    return "hi"


print(sayhi())
