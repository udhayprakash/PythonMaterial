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
        print("makebold - args", args)
        print("makebold  - kwargs", kwargs)
        print()
        return "<b>" + fn(*args, **kwargs) + "</b>"

    return wrapped


def makeitalic(fn):
    def wrapped(*args, **kwargs):
        print("makeitalic - args", args)
        print("makeitalic  - kwargs", kwargs)
        print()
        return "<i>" + fn(*args, **kwargs) + "</i>"

    return wrapped


@makeitalic
@makebold
def hello(name, salary=20000000):
    return "hello world:{}\t salary:{}".format(name, salary)


print(hello('udhay', 9000000))  ## returns "<b><i>hello world</i></b>"
# print('-'* 20)
# print(hello('udhay', salary=9000000))  ## returns "<b><i>hello world</i></b>"
