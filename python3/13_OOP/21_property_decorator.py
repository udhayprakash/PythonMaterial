#!/usr/bin/python
"""
Purpose: newly style classes better support property decorator

To access a method as a variable, we need property decorator

Q) When to use @property decorator?
Ans) When an attribute is derived from other attributes in the class, so the
     derived attribute will update whenever the source attributes is changed.

Q) How to make a @property?
Ans) Make an attribute as property by defining it as a function and add the
     @property decorator before the fn definition.

Q) When to define a setter method for the property?
Ans) Typically, if you want to update the source attributes whenever the property
    is set. It lets you define any other changes as well.
"""


class Person:
    def __init__(self, first_name, last_name):
        self.first = first_name
        self.last = last_name

    def email(self):
        return f'{self.first}.{self.last}@email.com'

    @property  # .getter
    def full_name(self):
        if self.first and self.last:
            return self.first + ' ' + self.last

    @full_name.setter
    def full_name(self, name):
        firstname, lastname = name.split()
        self.first = firstname
        self.last = lastname

    @full_name.deleter  # doesn't get called in old style classes
    def full_name(self):
        self.first = None
        self.last = None


person1 = Person('Udhay', 'Prakash')
print(person1.email())

# After placing property decorator, method
# should be accessed like a variable

print(f'person1.full_name  :{person1.full_name}')
# print(f'person1.full_name():{person1.full_name()}')
# TypeError: 'str' object is not callable


person1 = Person('Udhay', 'Prakash')
print(person1.email())

print(f'person1.first      :{person1.first}')
print(f'person1.last       :{person1.last}')
print(f'person1.full_name  :{person1.full_name}')
print()

# Updating the value
person1.full_name = 'Shyam Benegal'
print(f'person1.first      :{person1.first}')
print(f'person1.last       :{person1.last}')
print(f'person1.full_name  :{person1.full_name}')
print()

# Deleting fullname calls the deleter method, which erases self.first and self.last
del person1.full_name
# delattr(person1, full_name)

print(f'person1.first      :{person1.first}')
print(f'person1.last       :{person1.last}')
print(f'person1.full_name  :{person1.full_name}')
