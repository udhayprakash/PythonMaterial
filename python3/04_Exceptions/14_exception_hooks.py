#!/usr/bin/python3
"""
Purpose: Exception Hooks 
    - When exception is raised with excepthook set, 
        case 1: when exception is handled with except block,
                it works as ordinary exception handling
        case 2: When exception is not handled with except block, 
                exception hook function is executed, and program stops 
"""
import sys


def my_excepthook(exctype, value, traceback):
    print('\nUnhandled error')
    print('\tType     :', exctype)
    print('\tValue    :', value)
    print('\tTraceback:', traceback)


sys.excepthook = my_excepthook

print('Before exception')

# case 1
# 1 / 0

# case 2
try:
    1 / 0
except ZeroDivisionError as ex:
    print(f'{ex=}')

# case 3
raise RuntimeError('case3: This is error message')

print('After exception')
