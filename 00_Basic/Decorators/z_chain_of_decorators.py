#!/usr/bin/python
def makebold(fn):
    def wrapped(*args, **kwargs):
        return "<b>" + fn() + "</b>"
    return wrapped

def makeitalic(fn):
    def wrapped(*args, **kwargs):
        return "<i>" + fn() + "</i>"
    return wrapped

@makebold
@makeitalic
def hello():
    return "hello world"

print hello() ## returns "<b><i>hello world</i></b>"