#!/usr/bin/python
"""
Purpose:

NOTE: This is best practice to define all the instance variables
      in the constructor, for better memory management
"""


# class Shape:
class Shape(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.description = ''
        self.author = ''

    def perimeter(self):
        return 2 * self.x + 2 * self.y

    def describe(self, text):
        self.description = text

    def author_name(self, name):
        self.author = name

    def scale_size(self, scale):
        (self.x, self.y) = (self.x * scale, self.y * scale)


rectangle = Shape(100, 45)  # instantiation

print('rectangle.x', rectangle.x)
print("type(Shape)     ", type(Shape))
print("type(rectangle) ", type(rectangle))

print("dir(rectangle) ", dir(rectangle))

print(rectangle.perimeter())
rectangle.describe("wide rectangle more than twice as wide as tall")
