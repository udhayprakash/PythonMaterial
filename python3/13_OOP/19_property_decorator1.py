#!/usr/bin/python
"""
Purpose: newly style classes better support property decorator

To access a method as a variable, we need property decorator

"""


class Person:
    def __init__(self, first_name, last_name):
        self.first = first_name
        self.last = last_name

    def email(self):
        return f'{self.first}.{self.last}@email.com'

    @property
    def full_name(self):
        return self.first + ' ' + self.last


person1 = Person('Udhay', 'Prakash')
print(person1.email())

# After placing property decorator, method
# should be accessed like a variable

print(f'person1.full_name  :{person1.full_name}')
# print(f'person1.full_name():{person1.full_name()}')
# TypeError: 'str' object is not callable

