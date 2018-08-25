#!/usr/bin/env python

class Car:
    a = 1
    _a = 2  # protected
    __a = 3  # private variable

    def __init__(self):
        self.__updateSoftware()

    def drive(self):
        print 'driving'

    def __updateSoftware(self):
        print 'updating software'


redcar = Car()
redcar.drive()
# redcar.__updateSoftware()  #not accesible from object.

print dir(Car)

print '----------------'
redcar._Car__updateSoftware()
print redcar._Car__a
