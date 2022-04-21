#!/usr/bin/python
"""
Purpose: __call__ method importance
"""


class MyClass:
    def __init__(self):
        print('Constructor is called')

    def __str__(self):
        return 'This is instance of MyClass'

    def __call__(self, *args, **kwargs):
        """ Used to make the instance callable"""
        print('This is called')

m = MyClass()
print(m)

print(f'callable(m):{callable(m)}')
m()
