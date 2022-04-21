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
        return '%s has reached %s' % (self.name, self.distance)

# # Instantiation
# r = Rocket('PSLV-4', 7887)

class MarsRoverComp:
    def __init__(self, name, distance, maker):
        self.rocket = Rocket(name, distance)  # instantiating the base

        self.maker = maker

    def get_maker(self):
        return '%s Launched by %s' % (self.rocket.name, self.maker)


if __name__ == '__main__':
    m = MarsRoverComp('mars_rover2', 'till Mars', 'ISRO')
    # for each_attribute in dir(m):
    #     print(each_attribute)

    print(m.rocket)
    print(dir(m.rocket))
    print(f'm.rocket.distance:{m.rocket.distance}')
    print(f'm.rocket.name    :{m.rocket.name}')
    print(m.rocket.launch())

    print(f'm.maker          :{m.maker}')
    print(m.get_maker())

    print(f'{MarsRoverComp.__mro__ =}')
    # (<class '__main__.MarsRoverComp'>, <class 'object'>)
