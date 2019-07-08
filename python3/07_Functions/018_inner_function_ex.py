#!/usr/bin/python
"""
Purpose: Inner function example
"""

def outer():
    print('In outer function')
    nnum = 345
    mytuple = (1, 2, 3)
    mylist = [1, 2, 3]
    mydict = {'1': 1}

    def inner():
        print('In inner function', nnum)

    inner()

outer()

# inner()  # NameError: name 'inner' is not defined

# print(nnum)  # NameError: name 'nnum' is not defined
# print(mytuple) # NameError: name 'mytuple' is not defined
# print(mylist)
# print(mydict)