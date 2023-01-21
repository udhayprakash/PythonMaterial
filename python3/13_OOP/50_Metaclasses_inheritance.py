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


if __name__ == "__main__":
    # Method 1 - Class-Level Changes
    k1 = Mascot("Mango")
    print(f"{Mascot.__bases__ =}")
    try:
        Mascot.__bases__ += (CuteMixin,)  # WORKS ONLY IN PYTHON 2
    except Exception as ex:
        print(ex)
    else:
        k1.be_cute()

    # Method 2 - Instance-Level Changes
    k2 = Mascot("apple")
    k2.__class__ = type("someNewType", (Mascot, CuteMixin), {})
    k2.be_cute()
