#!/usr/bin/python
"""
Purpose: OOP demos
"""
__author__ = 'Developer Name'


class Name:
    def __init__(self):
        """
        This is a constructor method.
        """
        print('I am a constructor. ')
        print('I will be called, the moment you create an instance')
        self.s = ''

    def display_names(self): 
        """
        This is an instance method.
        """
        print('Existing names: ramesh, suresh, mahesh, ganesh')
        self.s = 'Something'


n = Name() # Name.__init__(n)
Name()

print('n=     ', n)
print(('dir(n) ', dir(n)))
print(('vars(n)', vars(n)))
help(n)

# we need to call all other methods, except constructor
n.display_names()

n.__init__()

print((Name.display_names(n)))