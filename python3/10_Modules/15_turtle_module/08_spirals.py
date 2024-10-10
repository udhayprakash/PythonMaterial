#!/usr/bin/python

from turtle import bgcolor, colormode, exitonclick, fd, pencolor, rt, speed
import secrets

bgcolor("black")
x = 1
speed(0)

while x < 400:
    r = secrets.SystemRandom().randint(0, 255)
    g = secrets.SystemRandom().randint(0, 255)
    b = secrets.SystemRandom().randint(0, 255)

    colormode(255)
    pencolor(r, g, b)
    fd(50 + x)
    rt(90.991)
    x = x + 1

exitonclick()
