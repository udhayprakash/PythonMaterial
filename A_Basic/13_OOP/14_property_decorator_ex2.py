"""
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
        
    @fullname.deleter # doesn't get called in old style classes 
    def fullname(self):
        self.first = None
        self.last = None        
        
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)
    
# Init a Person 
person = Person('Udhay', 'Prakash')
print(person.fullname)  #> Udhay Prakash

# Deleting fullname calls the deleter method, which erases self.first and self.last
del person.fullname 

# Print the changed values of `first` and `last`
print(person.first)  #> None
print(person.last)  #> None