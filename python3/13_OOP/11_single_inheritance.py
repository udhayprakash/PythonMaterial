#!/usr/bin/python
"""
Purpose: Single Inheritance

    One Parent
    Two child

"""


class Cars:
    def __init__(self, name, chs, eng):
        self.chasis = chs
        self.engine = eng
        self.car_name = name
        print("\nCar Constructor - Initializing Car %s" % self.car_name)

    def Get_Chasis(self):
        print("Chasis for the car %s is : %d" % (self.car_name, self.chasis))

    def Get_Engine(self):
        print("Engine for the car %s is : %d" % (self.car_name, self.engine))

    def hello(self):
        print("I am Cars class")


class Bmw(Cars):
    def __init__(self, name, chs, eng, auto_gear='Non Available'):
        Cars.__init__(self, name, chs, eng)
        self.auto_gear = auto_gear
        print("BMW Constructor - Initializing Car %s" % name)

    def Auto_Gear(self):
        print("Auto Gear availability : %s" % self.auto_gear)

    def hello(self):
        print('I am Bmw class')


class Volvo(Cars):
    def __init__(self, name, chs, eng, auto_driving):
        Cars.__init__(self, name, chs, eng)
        self.auto_driving = auto_driving
        print("Volvo Constructor - Initializing Car %s" % name)

    def Auto_Drive(self):
        print("Auto Driving availability : %s" % self.auto_driving)

    def hello(self):
        print('I am a Volvo class')


car1 = Bmw('AB121', 142211, 908790, 'Available')
print(dir(car1))
car1.Get_Chasis()
car1.Get_Engine()

car1.Auto_Gear()
car1.hello()

car2 = Volvo('V189B', 22222, 33333, 'Not Available')
car2.Get_Chasis()
car2.Get_Engine()

car2.Auto_Drive()
car2.hello()

# Method Resolution Order
print(Cars.__mro__)
# (<class '__main__.Cars'>, <class 'object'>)

print(Bmw.__mro__)
# (<class '__main__.Bmw'>, <class '__main__.Cars'>, <class 'object'>)

print(Volvo.__mro__)
# (<class '__main__.Volvo'>, <class '__main__.Cars'>, <class 'object'>)
