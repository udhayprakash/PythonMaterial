#!/usr/bin/python
"""
Purpose:
In composition, we do not inherit from the base class 
but establish relationships between classes through the 
use of instance variables that are references to other objects. 
"""


class Rocket:
    def __init__(self, name, distance):
        self.name = name
        self.distance = distance

    def launch(self):
        return "%s has reached %s" % (self.name, self.distance)


class MarsRoverComp:
    def __init__(self, name, distance, maker):
        self.rocket = Rocket(name, distance)  # instantiating the base

        self.maker = maker

    def get_maker(self):
        return "%s Launched by %s" % (self.rocket.name, self.maker)


if __name__ == "__main__":
    z = MarsRoverComp("mars_rover2", "till Mars", "ISRO")
    print(dir(z))
    print(dir(z.rocket))
    print(z.rocket.launch())
