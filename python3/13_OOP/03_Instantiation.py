#!/usr/bin/python
"""
Purpose: Understanding Class instantiation
"""

# Class Definition
class MyClassName:
    number = 786  # class Variables

    def hello_world(self):  # methods
        return "Hello world"


# Instantiation
c1 = MyClassName()
print(f"c1: {c1}")

# print(dir(c1))
# ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__',
# '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__',
# '__hash__', '__init__', '__init_subclass__', '__le__',
# '__lt__', '__module__', '__ne__', '__new__', '__reduce__',
# '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__',
# '__str__', '__subclasshook__', '__weakref__'
# 'hello_world', 'number]

print(f"callable(c1.number)     :{callable(c1.number)}")

print(f"c1.number               :{c1.number}")
# print(f'c1.number2              :{c1.number2}')
# AttributeError: 'MyClassName' object has no attribute 'number2'

print(f'getattr(c1, "number")   :{getattr(c1, "number")}')

print(f'\nhasattr(c1, "number")   :{hasattr(c1, "number")}')
print(f"'number' in dir(c1)     :{'number' in dir(c1)}")

c1.number = 1000
print(f'\ngetattr(c1, "number")   :{getattr(c1, "number")}')

setattr(c1, "number", 3333)
print(f'getattr(c1, "number")   :{getattr(c1, "number")}')

delattr(c1, "number")  # classes are mutable objects
# del c1.number

print(f"\ncallable(c1.hello_world):{callable(c1.hello_world)}")
print(f"c1.hello_world          :{c1.hello_world}")
print(f"c1.hello_world()        :{c1.hello_world()}")

assert c1.hello_world() == MyClassName.hello_world(c1)

# ----------------------


class EmptyClass:
    pass


e1 = EmptyClass()
print()  # check  for user-defined objects
print(f"isinstance(c1, MyClassName) :{isinstance(c1, MyClassName)}")  # True
print(f"isinstance(c1, MyClassName) :{isinstance(c1, EmptyClass)}")  # False
print(f"isinstance(e1, EmptyClass)  :{isinstance(e1, EmptyClass)}")  # True

print()  # Check for builtin objects
print(f"isinstance(123, int)        :{isinstance(123, int)}")  # True
print(f"isinstance(123.9, int)      :{isinstance(123.9, int)}")  # False
print(f"isinstance(123.9, float)    :{isinstance(123.9, float)}")  # True
print(f"isinstance(123.9, str)      :{isinstance(123.9, str)}")  # False

num1 = 123
print(f"\nisinstance(num1, int):{isinstance(num1, int)}")
print(f"type(num1) is int    :{type(num1) is int}")
print(f"type(num1) == int    :{type(num1) == int}")  # not recommended
