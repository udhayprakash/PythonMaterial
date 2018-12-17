#!/usr/bin/python
"""
Purpose: OOP demos
"""
__author__ = 'Developer Name'

# __new__
class Name:
    my_class_variable = 'something'
    def __init__(self):  # constructor
        print('I am a constructor. ')
        print('I will be called, the moment you create an instance')
        self.a = 'apple'
        # retunn should not be present for constructor

    def my_instance_method(self):
        print "my instance method"

n = Name()
m = Name()
p = Name  # class object assignment

p()


print
print '----------calling contructor'
n.__init__()

print 'vars()', vars()
# Note: calling the vars() function without parameters will return a dictionary containing the local symbol table.


print '='*10
print 'n.__dict__', n.__dict__
print 'vars(n)', vars(n) # instance variables, not methods

"""
run below in shell
vars(list)
vars(str)
vars(dict)
"""
