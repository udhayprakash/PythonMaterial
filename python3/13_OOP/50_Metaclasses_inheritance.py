#!/usr/bin/python3
"""
Purpose: INheritance Using Metaclasses
    using type() function
"""


class CuteMixin:
    def be_cute(self):
        print("cuteMixin- be_cute")


class Mascot:
    def __init__(self, name):
        self.name = name


if __name__ == '__main__':
    # Method 1 - Instance-Level Changes
    k = Mascot("apple")
    k.__class__ = type('someNewType', (Mascot, CuteMixin), {})
    k.be_cute()

    # Method 2 - Class-Level Changes
    k2 = Mascot("Mango")
    print(Mascot.__bases__)
    Mascot.__bases__ += (CuteMixin,)  # WORKS ONLY IN PYTHON 2
    k2.be_cute()
