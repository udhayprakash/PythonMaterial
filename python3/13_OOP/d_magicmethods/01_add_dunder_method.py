#!/usr/bin/python
"""
Purpose: Dunder( Double underscore) Methods

"""
num1 = 100
print(num1 + 22)
print(num1.__add__(22))

assert num1 + 22 == num1.__add__(22)


class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __add__(self, other):
        return Person(self.name, other.surname)

    def __repr__(self) -> str:
        # return f'{self.name} {self.surname}'
        return " ".join((self.name, self.surname)).title()


father = Person("FatherName", "FatherSurname")
print(father)


mother = Person("MotherName", "MotherSurname")
print(mother)

print()
print(mother + father)
print(mother.__add__(father))
