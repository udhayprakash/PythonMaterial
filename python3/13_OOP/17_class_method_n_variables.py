#!/usr/bin/python
"""
Purpose: Class Method
"""


class Robot:
    """
    Represents a robot, with a name.
    """
    # A class variable, counting the number of robots
    population = 0

    def __init__(self, name):
        """
        INITIALIZES THE DATA.
        :param name:
        """
        self.name = name
        print("\n(Initializing {})".format(self.name))

        Robot.population += 1

    def __del__(self):
        """
        I am dying.
        :return:
        """
        print("\n{} is being destroyed:".format(self.name))
        Robot.population -= 1
        if Robot.population == 0:
            print("{} was the lst one.".format(self.name))
        else:
            print("There are still {:d} robots working.".format(Robot.population))

    def say_hi(self):
        """
        Greeting by the robot.
        Yeah, they can do that.
        :return:
        """
        print("Greetings, my masters call me {}".format(self.name))

    @classmethod
    def how_many(cls):
        """
        Prints the current population.
        :return:
        """
        print("\tWe have {:d} robots.".format(cls.population))  # Robot.population


if __name__ == '__main__':
    chitti = Robot('chitti')
    chitti.say_hi()
    Robot.how_many()

    irobo = Robot('irobo')
    irobo.say_hi()
    Robot.how_many()

    # Delete an instance
    del chitti

    droid = Robot('R2-D2')
    droid.say_hi()
    Robot.how_many()
