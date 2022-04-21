#!/usr/bin/python
"""
Purpose: To draw a square shape using turtle
"""
import turtle

my_turtle = turtle.Turtle()

for i in range(4):
    my_turtle.forward(50)
    my_turtle.right(90)

turtle.done()
