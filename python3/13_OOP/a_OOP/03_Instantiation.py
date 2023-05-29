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
print(f"{id(c1) = }")
print(f"{dir(c1) = }")
print()

print(f"callable(c1.number)     :{callable(c1.number)}")
print(f"c1.number               :{c1.number}")

# print(f'c1.number2              :{c1.number2}')
# AttributeError: 'MyClassName' object has no attribute 'number2'. Did you mean: 'number'?

print(f'getattr(c1, "number")   :{getattr(c1, "number")}')

# checks
print(f'\nhasattr(c1, "number")   :{hasattr(c1, "number")}')
print(f"'number' in dir(c1)     :{'number' in dir(c1)}")

# classes are mutable objects
c1.number = 1000
print(f'\ngetattr(c1, "number")   :{getattr(c1, "number")}')
print(f"{id(c1) = }")


setattr(c1, "number3", 3333)
print(f'getattr(c1, "number3")   :{getattr(c1, "number3")}')

c1.number4 = 4444
print(f'getattr(c1, "number4")   :{getattr(c1, "number4")}')
print(f"{dir(c1) = }")


delattr(c1, "number")
del c1.number3
print(f"{dir(c1) = }")

print(f"{c1.number =}")
# print(f"{c1.number3 =}")  # AttributeError

delattr(c1, "number4")
# print(f"{c1.number4 =}")  # AttributeError

"""
NOTE: Both delattr and del can delete any attribute, except onces
defined in class definition

"""
print()

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
