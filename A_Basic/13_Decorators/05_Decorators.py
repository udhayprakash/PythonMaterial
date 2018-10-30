#!/usr/bin/python
"""
Purpose: chain of decorators

NOTE:
----
Decorators were introduced in Python 2.4, so be sure your code will be run on >= 2.4.
Decorators slow down the function call. Keep that in mind.
"""


def makebold(fn):
    def wrapped(*args, **kwargs):
        print "makebold - args", args
        print "makebold  - kwargs", kwargs

        return "<b>" + fn() + "</b>"

    return wrapped


def makeitalic(fn):
    def wrapped(*args, **kwargs):
        print "makeitalic - args", args
        print "makeitalic  - kwargs", kwargs

        return "<i>" + fn() + "</i>"

    return wrapped


@makebold#('first')
@makeitalic#('second')
def hello():
    return "hello world"


print hello()  ## returns "<b><i>hello world</i></b>"
