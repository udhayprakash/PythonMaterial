#!/usr/bin/env python

class Car:
    a = 1   # public class variable
    _a = 2  # protected class variable
    __a = 3  # private class variable

    def __init__(self): 
        self.__updateSoftware()

    def drive(self):     # public instance method
        print('driving')

    def _cleaning(self):  # protected instance method
        print('cleaning')

    def __updateSoftware(self): # private instance method
        print('updating software')


redcar = Car()

# Accessing public method
redcar.drive()

# Accessing protected method
redcar._cleaning()

# Accessing private method
# redcar.__updateSoftware()  #not accesible from object.
redcar._Car__updateSoftware()


print(dir(Car))

print('----------------')
redcar._Car__updateSoftware()
print(redcar._Car__a)
