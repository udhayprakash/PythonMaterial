#!/usr/bin/python
"""
Purpose: demo of OOP
"""

class Person:
    def __init__(self):         # instance methods
        """
        This is constructor
        """
        self.name = ''          # instance variables
        self.age = 0

    def enterAge(self, age):    # instance methods
        self.age = age

    def displayAge(self):       # instance methods
        print('Person age is %d' % self.age)

    def enterName(self, name): # instance methods 
        self.name = name

    def displayName(self):      # instance methods
        print('Person name is ' + self.name)


p = Person()

print(dir(p))

p.displayAge()
p.enterAge(23)
p.displayAge()

p.displayName()
p.enterName('Ramesh')
p.displayName()
