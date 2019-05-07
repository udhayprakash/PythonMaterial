#!/usr/bin/python
"""
Without decorators
"""


def div(a, b): 
    try:
        a / b
    except Exception as e:
        return repr(e)
    else:
        return a / b


def add(a, b):
    try:
        a + b
    except Exception as e:
        return repr(e)
    else:
        return a + b


print('div(4, 2)', div(4, 2))
print('div(4, 0)', div(4, 0))

print('add(2, 3)', add(2, 3))
print("add('a', 3)", add('a', 3))
