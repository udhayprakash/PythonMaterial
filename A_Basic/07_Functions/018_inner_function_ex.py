#!/usr/bin/python
"""
Purpose: Inner function example
"""

def outer():
    print 'In outer function'
    nnum = 786

    def inner():
        print 'In Inner function', nnum

    inner()


outer()

# inner()  # NameError: name 'inner' is not defined
#
# print nnum  # NameError: name 'nnum' is not defined
