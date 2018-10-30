#!/usr/bin/env python

class Car:
    a = 1
    _a = 2  # protected
    __a = 3  # private variable

    def __init__(self):
        self.__updateSoftware()

    def drive(self):
        print 'driving'

    def _cleaning(self):
        print 'cleaning'

    def __updateSoftware(self): # private instance method
        print 'updating software'


redcar = Car()

# Accessing public method
redcar.drive()

# Accessing protected method
redcar._cleaning()

# Accessing private method
# redcar.__updateSoftware()  #not accesible from object.
redcar._Car__updateSoftware()


print dir(Car)

print '----------------'
redcar._Car__updateSoftware()
print redcar._Car__a
