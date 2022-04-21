#!/usr/bin/python3
"""
Purpose:
    An abstract class exists only so that other "concrete"
    classes can inherit from the abstract class.

"""

from abc import ABC, abstractmethod


class Animal(ABC):
    def move(self):
        pass


class Human(Animal):
    def move(self):
        print("I can walk and run")


class Snake(Animal):
    def move(self):
        print("I can crawl")


class Dog(Animal):
    def move(self):
        print("I can bark")


class Lion(Animal):
    def move(self):
        print("I can roar")


# Driver code
R = Human()
R.move()

K = Snake()
K.move()

R = Dog()
R.move()

K = Lion()
K.move()

# Output:

# I can walk and run
# I can crawl
# I can bark
# I can roar
