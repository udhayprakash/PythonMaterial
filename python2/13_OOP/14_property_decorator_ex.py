"""
newly stye classes better support property decorator
"""

class Person(object):
    def __init__(self, firstname, lastname):
        self.first = firstname
        self.last = lastname

    @property    
    def fullname(self):
        return self.first + ' '+ self.last

    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)


person = Person('Udhay', 'Prakash')
print(person.fullname)  #()

person.last = 'chaitanya'

print(person.fullname) 

# person.fullname = 'raja ram'
# print 'person.fullname', person.fullname
# print 'person.first', person.first 
# # But, 'self.first' and 'self.last' are not changed

