#!/usr/bin/python
"""
Purpose: demo of OOP
"""


class Person:
    def __init__(self):
        """
        This is constructor
        """
        self.name = 'Suresh'  # ''
        self.age = 99  # 0

    def enterAge(self, age):
        self.age = age

    def displayAge(self):
        print('Person age is ', self.age)

    def enterName(self, name):
        self.name = name

    def displayName(self):
        print('Person name is ', self.name)


p = Person()

print(dir(p))

p.displayAge()
p.enterAge(23)
p.displayAge()

p.displayName()
p.enterName('Ramesh')
p.displayName()
