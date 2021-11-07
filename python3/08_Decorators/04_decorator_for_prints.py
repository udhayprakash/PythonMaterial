#!/usr/bin/python3
"""
Purpose: Decorator for printing start and end of function
"""


def addition(num1, num2):
    print('function -start ')
    result = num1 + num2
    print('function - before end')
    return result


def multiplication(num1, num2, num3):
    print('function -start ')
    result = num1 * num2 * num3
    print('function - before end')
    return result


print(addition(12, 34))
print(multiplication(12, 34, 10))

print('\n###### USING DECORATORS  ############')


# def print_function(func):
#     def inner(*args, **kwargs):
#         print('function - start ')
#         result1 = func(*args, **kwargs)
#         print('function - before end')
#         return result1
#
#     return inner

def print_function(func):
    def inner(*args, **kwargs):
        print(f'{func.__name__} function - start ')
        result1 = func(*args, **kwargs)
        print(f'{func.__name__} function - before end')
        return result1

    return inner


@print_function
def addition1(num1, num2):
    result = num1 + num2
    return result


@print_function
def multiplication1(num1, num2, num3):
    result = num1 * num2 * num3
    return result


print()
print(addition1(12, 34))
print(multiplication1(12, 34, 10))
