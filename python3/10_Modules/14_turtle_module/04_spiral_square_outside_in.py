#!/usr/bin/python
"""
Purpose: spiral square outside in
"""
import turtle  # Outside_In

wn = turtle.Screen()
wn.bgcolor("light green")
wn.title("myTurtle")
skk = turtle.Turtle()
skk.color("blue")


def sqrfunc(size):
    for i in range(4):
        skk.fd(size)
        skk.left(90)
        size = size - 5


sqrfunc(146)
sqrfunc(126)
sqrfunc(106)
sqrfunc(86)
sqrfunc(66)
sqrfunc(46)
sqrfunc(26)

# waits for the user to close the window
turtle.done()
