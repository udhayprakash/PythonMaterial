"""
newly style classes better support property decorator
"""


class Person(object):
    def __init__(self, firstname, lastname):
        self.first = firstname
        self.last = lastname

    @property
    def fullname(self):
        return self.first + ' ' + self.last

    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)


person = Person('Udhay', 'Prakash')
print(person.email())
print('person.first', person.first)
print('person.last ', person.last)

print(vars(person))
# print(person.fullname())

# After placing property decorator, method
# should be accessed like a variable

print(f'person.fullname:{person.fullname}')

person.last = 'chaitanya'
print(f'person.fullname:{person.fullname}')
