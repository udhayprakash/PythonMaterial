#!/usr/bin/python
"""
Purpose:
    Implementing C++ style printing syntax
"""


class Cout:
    def __lshift__(self, other):
        print(other, end="")
        return self

    def __rrshift__(self, other):
        print(other, end="")
        return self


class Endl:
    def __rshift__(self, other):
        return other + "\n"

    def __str__(self):
        return "\n"


cout = Cout()
endl = Endl()

cout << "C++ printing in python" << endl
endl >> "Works even this way!" >> cout
