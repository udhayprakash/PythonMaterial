#!/usr/bin/python
"""
Purpose: decorator example
"""


def addition(num1, num2):
    print('function -start ')
    result = num1 + num2
    print('function - before end')
    return result


def multiplication(num1, num2):
    print('function -start ')
    result = num1 * num2
    print('function - before end')
    return result


print(addition(12, 34))
print(multiplication(12, 34))

print('\n###### USING DECORATORS  ############')


def print_function(func):
    def inner(*args, **kwargs):
        print('function -start ')
        print('function - before end')
        return func(*args, **kwargs)

    return inner


@print_function
def addition1(num1, num2):
    return num1 + num2


@print_function
def multiplication1(num1, num2):
    return num1 * num2


print(addition1(12, 34))
print(multiplication1(12, 34))
