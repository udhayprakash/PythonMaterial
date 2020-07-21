#!/usr/bin/python
"""
Purpose: To draw spiral shape using turtle
"""
import turtle

my_turtle = turtle.Turtle()
myWin = turtle.Screen()


def draw_spiral(_my_turtle, line_length):
    if line_length > 0:
        _my_turtle.forward(line_length)
        _my_turtle.right(90)
        draw_spiral(_my_turtle, line_length - 5)


draw_spiral(my_turtle, 100)
myWin.exitonclick()
