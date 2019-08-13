#!/usr/bin/python
"""
Without decorators
"""

# def div(a,b):
#     return a/b

def div(a, b):
    try:
        a/b
    except Exception as ex:
        return repr(ex)
    else:
        return a/b

print('div(4, 2)  ', div(4, 2))
print('div(4, 0)  ', div(4, 0))


# def add(str1, str2):
#     return str1 + str2 

def add(str1, str2):
    try:
        str1 + str2
    except Exception as ex:
        return repr(ex)
    else:
        return str1 + str2

print('add(2, 3)  ', add(2, 3))
print("add('a', 3)", add('a', 3))
