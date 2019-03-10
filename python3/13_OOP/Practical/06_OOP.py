#!/usr/bin/python
"""
Purpose: demo of OOP
"""


class Person:
    def __init__(self):  # constructor method
        """
        This is constructor
        """
        self.name = ''  # instance variables
        self.age = 0  # instance variables

    def enter_age(self, age):  # instance methods
        self.age = age

    def display_age(self):  # instance methods
        print('Person age is %d' % self.age)

    def enter_name(self, name):  # instance methods
        self.name = name

    def display_name(self):  # instance methods
        print('Person name is ' + self.name)


p = Person()

print(dir(p))

p.display_age()
p.enter_age(23)
p.display_age()

p.display_name()
p.enter_name('Ramesh')
p.display_name()


print callable(p.age)
print callable(p.display_age)
