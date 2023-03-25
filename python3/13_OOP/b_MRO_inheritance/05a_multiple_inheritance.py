#!/usr/bin/python3
"""
Purpose: Multiple Inheritance

    two parents
    one child

NOTE: All the instance variables must be created in constructor - PEP 8
"""
from pprint import pp


class A:
    def __init__(self):
        print("A - Base Class Contructor")
        super(A, self).__init__()
        print("<A>")
        self.x = 10
        self._x = 10
        self.__x = 10


class B:
    def __init__(self):
        print("B - Other Base class Constructor")
        super(B, self).__init__()
        print("<B>")
        self.y = 20
        self._y = 20
        self.__y = 20


class C(A, B):
    def __init__(self):
        print("C - Derived Class Constructor")
        # A.__init__()
        # B.__init__()
        super(C, self).__init__()  # Based on MRO order
        # super().__init__()
        print("<C>")
        self.z = 30
        self._z = 30
        self.__z = 30

        # print(f"{self.__x =}") # AttributeError
        print(f"{self._A__x =}")


c_instance = C()
pp(vars(c_instance))
"""
{
    'y': 20,  '_y': 20,  '_B__y': 20,
    'x': 10,  '_x': 10,  '_A__x': 10,
    'z': 30,  '_z': 30,   '_C__z': 30
}
"""


"""
NOTE:
    Instead of manually executing constructor methods of each Base class,
    super() will do based on MRO order

    Private Classes/ Methods of each class can be accessed directly from that class only.
    To access from other classes, we need to prepend _OwnerClass name

"""
