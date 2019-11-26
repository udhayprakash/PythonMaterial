#!/usr/bin/python
"""
Purpose: OOP demos

 constructor is a method which will be called the moment instance
    is created
"""
__author__ = 'Developer Name'


# class Definition
class Person:
    my_class_var = 111

    def __init__(self):
        print('New instance is born !!!')
        self.inst_var = 222
        local_var = 333
        # NOTE: Construction should return only None

    def instance_method(self):
        return 'This is an instance method'


# Instantiation
p1 = Person()
print(p1)

assert p1.instance_method() == Person.instance_method(p1)
print(f'p1.instance_method():{p1.instance_method()}')

# p1.__init__() # But NOT RECOMMEND, as code duplicate execution


print(dir(p1))

# To get only the instance variables
print(f'p1.__dict__: {p1.__dict__}')
print(f'vars(p1)   : {vars(p1)}')

assert vars(p1) == p1.__dict__

from pprint import pprint
print('vars(Person):')
pprint(vars(Person))
# -------------------------------------------------

pprint(vars())

# Note: calling the vars() function without parameters will
# return a dictionary containing the local symbol table.


"""
Assignment:
    run below in shell
    vars(list)
    vars(str)
    vars(dict)
"""
