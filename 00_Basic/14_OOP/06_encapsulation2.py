#!/usr/bin/env python
 
class Car:
 
    __maxspeed = 0
    __name = ""
 
    def __init__(self):
        self.__maxspeed = 200
        self.__name = "Supercar"
 
    def drive(self):
        print 'driving. maxspeed ' + str(self.__maxspeed)
 
    def setMaxSpeed(self,speed):
        self.__maxspeed = speed
 
redcar = Car()
redcar.drive()
redcar.setMaxSpeed(320)
redcar.drive()