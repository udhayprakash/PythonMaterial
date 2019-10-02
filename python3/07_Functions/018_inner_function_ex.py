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
        print('In inner function', mytuple)
        print('In inner function', mylist)
        print('In inner function', mydict)

    inner()


outer()

# inner()
# print(nnum)
# print(mytuple)
# print(mylist)
# print(mydict)
