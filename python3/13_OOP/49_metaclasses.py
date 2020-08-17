#!/usr/bin/python3
"""
Purpose: Metaclasses
    - Used for creating classes dynamically
    - useful for code injections
"""

# Method 1: creating class & instance ordinarily
class NewType(object):
    x = 'hello'


n2 = NewType()
print(f'{n2.x =}')  # 'hello'


# Method 2: Creating class & instance using metaclasses
NewType = type("NewType", (object,), {"x": "hello"})
n1 = NewType()
print(f'{n1.x =}')  # 'hello'


print(f'{n1 = } {id(n1) =}')
print(f'{n2 = } {id(n2) =}')

print('\n\n Anonymous types')

MyClass = type('', (object,), {'x': 'blah'})
print(f'{MyClass =}')  # <class '__main__.'>

my_inst = MyClass()
print(f'{my_inst.x =}')
