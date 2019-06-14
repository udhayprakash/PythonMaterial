#!/usr/bin/python
"""
Purpose: Inner function example
"""

def outer():
    print('In outer function')
    nnum = 786
    mytuple = (12, 2, 23)
    mylist = [23, 23, 234]
    mydict = {1:3, 23:3}
    def inner():
        print('In Inner function', nnum)

    inner()


outer()

# inner()  # NameError: name 'inner' is not defined

# print(nnum)  # NameError: name 'nnum' is not defined
# print(mytuple) # NameError: name 'mytuple' is not defined
# print(mylist)
# print(mydict)