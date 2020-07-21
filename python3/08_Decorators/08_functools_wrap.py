#!/usr/bin/python
"""
Purpose: functools.wrap importance
"""
import functools
# print(dir(functools))

print('\n\n case 0 ===============================')

def f(x):
    """does some math"""
    return x + x * x


print(f(2))
print(f'f.__name__:{f.__name__}')
print(f'f.__doc__ :{f.__doc__}')

print('\n\n case 1 ===============================')

def logged(func):
    def with_logging(*args, **kwargs):
        """ with logging doc"""
        print(func.__name__ + " was called")
        print(func.__doc__ + " is func doc")
        return func(*args, **kwargs)

    return with_logging


def f(x):
    """does some math"""
    return x + x * x


f = logged(f)

print(f'f.__name__:{f.__name__}')
print(f'f.__doc__ :{f.__doc__}')
f(2)

print('\n\n case 2 ===============================')

@logged
def f(x):
    """does some math"""
    return x + x * x


print(f'f.__name__:{f.__name__}')
print(f'f.__doc__ :{f.__doc__}')
f(2)
print('\n\n case 3 ===============================')
from functools import wraps

def logged(func):
    @wraps(func)
    def with_logging(*args, **kwargs):
        print(func.__name__ + " was called")
        return func(*args, **kwargs)

    return with_logging


@logged
def f(x):
    """does some math"""
    return x + x * x


print(f'f.__name__:{f.__name__}')  # 'f'
print(f'f.__doc__ :{f.__doc__}')  # 'does some math'
f(2)

# NOTE: 
# 1. wraps helps in retaining the properties of decorated function
# 2. @functools.wraps decorator uses the function functools.update_wrapper() 
#    to update special attributes like __name__ and __doc__ that are used 
#    in the introspection.
