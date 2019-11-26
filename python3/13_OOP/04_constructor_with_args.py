#!/usr/bin/python
"""
Purpose: Contructor with args
"""


class Animal:
    def __init__(self, name):
        self.name = name

    def walk(self):
        print(self.name + ' walks.')


if __name__ == '__main__':
    # duck = Animal()
    # TypeError: __init__() missing 1 required positional argument: 'name'

    duck = Animal('Duck')
    # Animal.__init__(duck, 'Duck')

    # TO retrive the instance variables
    print(vars(duck))
    print(f'duck.name:{duck.name}')

    # calling instance method
    duck.walk()

    # -------------------
    rhino = Animal('African Rhino')
    rhino.walk()
