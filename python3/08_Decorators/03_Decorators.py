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

print('\n===USING DECORATORS')
def print_statements(func):
    def inner(*args, **kwargs):
        print('function -start ')
        # print('In print_statemenst decorator', func)
        myresult = func(*args, **kwargs)
        print('function - before end')
        return myresult

    return inner


@print_statements
def addition11111(num1, num2):
    result = num1 + num2
    return result


@print_statements
def multiplication1111(num1, num2):
    result = num1 * num2
    return result


print(multiplication1111(12, 3))
print(addition11111(12, 34))
