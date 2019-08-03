#!/usr/bin/python
"""
Purpose: functools.wrap importance
"""

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
        print(func.__name__ + " was called")
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

print(f'f.__name__:{f.__name__}') # 'f'
print(f'f.__doc__ :{f.__doc__}')  # 'does some math'
f(2)

# NOTE: wraps helps in retaining the properties of 
# decorated function
