#!/usr/bin/python
"""
Purpose: OOP demos
"""
__author__ = 'Developer Name'

class Person:
    my_class_variable = 'SOmeThing'  # class variables

    def __init__(self):
        print('COnstructor method called')
        self.first_name = 'Human'
        self.last_name = 'Being'

    #NOTE: contructor method should have NOne as return 
    
    def my_instance_method(self):
        print('INstanace method called')

p1 = Person()
print(p1)

# Instance methods need to be called, to get executed
p1.my_instance_method()

# p1.__init__()  # But NOT RECOMMENED, as code deplicate execution

print(dir(p1))
print(f'p1.first_name:{p1.first_name}')
print(f'p1.first_name:{p1.first_name}')

print(vars(p1))
print(p1.__dict__)

assert vars(p1) == p1.__dict__

########################
from pprint import pprint
pprint(vars())

# Note: calling the vars() function without parameters will 
# return a dictionary containing the local symbol table.

"""
run below in shell
vars(list)
vars(str)
vars(dict)
"""


