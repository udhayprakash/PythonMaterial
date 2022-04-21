#!/usr/bin/python


import turtle
wn = turtle.Screen()
t = turtle.Turtle()
t.speed('fastest')
radius = 0
tick = 0
while True:
    tick+=1
    t.forward(tick)
    t.left(100+tick)
    t.forward(5)
    t.left(3)
    t.right(0+tick)
