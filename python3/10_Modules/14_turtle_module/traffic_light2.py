#!/usr/bin/python
"""
Purpose:
"""
import turtle


def drawLight(T, S, c):
    T.speed(1000)
    S.clear()
    T.penup()
    T.setpos(0, 0)
    T.pensize(12)
    if c == 1:
        T.color("black", "orange")
    else:
        T.color("black", "gray")
    T.pendown()
    T.begin_fill()
    T.circle(50)
    T.end_fill()
    T.penup()
    T.setpos(0, 210)
    if c == 0:
        T.color("black", "red")
    else:
        T.color("black", "gray")
    T.pendown()
    T.begin_fill()
    T.circle(50)
    T.end_fill()
    T.penup()
    T.setpos(0, -210)
    if c == 2:
        T.color("black", "green")
    else:
        T.color("black", "gray")
    T.pendown()
    T.begin_fill()
    T.circle(50)
    T.end_fill()
    T.penup()
    T.hideturtle()


S = turtle.Screen()
T = turtle.Turtle()
i = 1  # int(input("Enter color number\n"))
drawLight(T, S, i)
S.exitonclick()
