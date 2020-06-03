#!/usr/bin/python
"""
Purpose: Raising exception 
"""

# raise Exception()
# raise Exception('This is an Error')
# raise ValueError('This is an Error')
# raise TypeError('This is an Error')


try:
    num = eval(input('num ='))
    if num == 0:
        raise Exception('Not excepting a zero value')
except Exception as ex:
    print(f'{ex =}')
else:
    print(f'{123/num =}')