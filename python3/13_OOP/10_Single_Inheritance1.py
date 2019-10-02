#!/usr/bin/python

"""
Purpose: Single Inheritance
"""


class Cars:
    def __init__(self, name, chs, eng):
        self.chasis = chs
        self.engine = eng
        self.car_name = name
        print("Car Constructor - Initializing Car %s" % self.car_name)

    def Get_Chasis(self):
        print("Chasis for the car %s is : %d" % (self.car_name, self.chasis))

    def Get_Engine(self):
        print("Engine for the car %s is : %d" % (self.car_name, self.engine))

    def hello(self):
        print("I am Cars class")


class Bmw(Cars):
    def __init__(self, name, chs, eng, auto_gear):
        Cars.__init__(self, name, chs, eng)
        self.auto_gear = auto_gear
        print("BMW Constructor - Initializing Car %s" % name)

    def Auto_Gear(self):
        print("Auto Gear availability : %s" % self.auto_gear)

    def hello(self):
        print("I am Bmw class")


class Volvo(Cars):
    def __init__(self, name, chs, eng, auto_driving):
        Cars.__init__(self, name, chs, eng)
        self.auto_driving = auto_driving
        print("Volvo Constructor - Initializing Car %s" % name)

    def Auto_Drive(self):
        print("Auto Driving availability : %s" % self.auto_driving)

    def hello(self):
        print("I am Volvo class")


asd = Bmw('AB121', 142211, 908790, 'Available')
asd.Get_Chasis()
asd.hello()

zxc = Volvo('V189B', 22222, 33333, 'Not Available')
zxc.Get_Chasis()

zxc.Auto_Drive()
zxc.hello()
