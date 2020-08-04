#!/usr/bin/python3
"""
Purpose: Exception Hooks 
    - When exception is raised with excepthook set, 
        case 1: when exception is handled with except block,
                it works as ordinary exception handling
        case 2: When excetpion is not handled with except block, 
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

# Case 1
try:
    raise RuntimeError('This is the error message')
except Exception as ex:
    print(ex)

# Case 2
raise RuntimeError('This is the error message')

# 1 + '213'
print('After exception')
