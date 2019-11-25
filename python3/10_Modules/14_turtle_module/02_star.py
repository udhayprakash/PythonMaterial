#!/usr/bin/python
"""
Purpose: Star Shape using Turtle
"""
import turtle

star = turtle.Turtle()

for i in range(20):
    star.forward(50)
    star.right(144)

turtle.done()