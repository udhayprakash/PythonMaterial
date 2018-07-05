#!/usr/bin/python


class Shape(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def perimeter(self):
        return 2 * self.x + 2 * self.y

    def describe(self, text):
        self.description = text

    def authorName(self, name):
        self.author = name

    def scalesize(self, scale):
        (self.x, self.y) = (self.x * scale, self.y * scale)


rectangle = Shape(100, 45)  # instantiation

print 'rectangle.x', rectangle.x
print "dir(rectangle) ", dir(rectangle)
print "type(rectangle) ", type(rectangle)

print rectangle.perimeter()
print rectangle.describe("wide rectangle more than twice as wide as tall")
