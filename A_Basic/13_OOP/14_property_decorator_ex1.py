class Person(object):

    def __init__(self, firstname, lastname):
        self.first = firstname
        self.last = lastname

    @property    
    def fullname(self):
        return self.first + ' '+ self.last

    @fullname.setter
    def fullname(self, name):
        firstname, lastname = name.split()
        self.first = firstname
        self.last = lastname

    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

person = Person('Udhay', 'Prakash')
print(person.fullname)  #> Udhay Prakash
print(person.first)  #> Udhay
print(person.last)  #> Prakash

# Setting fullname calls the setter method and updates person.first and person.last
person.fullname = 'Shyam Benegal'

# Print the changed values of `first` and `last`
print(person.fullname) #> Shyam Benegal
print(person.first)  #> Benegal
print(person.last)  #> Benegal