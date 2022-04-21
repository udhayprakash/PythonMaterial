#!/usr/bin/python
"""
Purpose: closure example demo
"""

def outer():
    print('In outer function')
    nnum = 786

    def inner():
        print('In Inner function', nnum)

    return inner#()


result = outer()
print('result', result)
print('result()', result())

# inner()  # NameError: name 'inner' is not defined

# print nnum  # NameError: name 'nnum' is not defined
