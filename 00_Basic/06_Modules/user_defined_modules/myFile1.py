#!/usr/bin/python

"""
Purpose: Demo of user-defined modules
Arithmetic Operations

NOTE: placing , at the end of return
statement will convert the returning value to tuple

NOTE: Default return is None
"""

NUM1 = 20
NUM2 = 80


# function definitions

def addition(a, b):
    '''
    Purpose: Addition of two numbers
    input variables: a, b
    input types: int, int
    return type: int
    '''
    return a + b   

def subtraction(a, b):
    """
    Purpose: Subtraction of two numbers
    input variables: a, b
    input types: int, int
    return type: int
    """
    return a - b


def multiplication(p, q):
    """
    Purpose: Multiplication of two numbers
    input variables: a, b
    input types: int, int
    return type: int
    """
    return p * q


def division(m, n):
    """
    Purpose: Division of two numbers
    input variables: a, b
    input types: int, int
    return type: int
    """
    return m/float(n)

print '__name__=', __name__

if __name__ == '__main__':
    # function calls
    addResult =  addition(NUM1, NUM2)
    print 'addResult=', addResult
    print subtraction(NUM1, NUM2)
    print multiplication(NUM1, NUM2)
    print division(NUM1, NUM2)
