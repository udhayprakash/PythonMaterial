

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
        print "(Initializing {})".format(self.name)

        Robot.population+=1

    def die(self):
        """
        I am dying.
        :return:
        """
        print "{} is being destroyed:".format(self.name)
        Robot.population-=1
        if Robot.population == 0:
            print "{} was the lst one.".format(self.name)
        else:
            print "There are still {:d} robots working.".format(Robot.population)

    def say_hi(self):
        """
        Greeting by the robot.
        Yeah, they can do that.
        :return:
        """
        print "Greetings, my masters call me {}".format(self.name)

    @classmethod
    def how_many(cls):
        """
        Prints the current population.
        :return:
        """
        print "We have {:d} robots.".format(cls.population)


droid1 = Robot("R2-D2")
droid1.say_hi()
Robot.how_many()

droid2 = Robot("C-3PO")
droid2.say_hi()
Robot.how_many()

print "\nRobots can do some work here.\n"

print "Robots have finished their work. So, let's destroy them..."

droid1.die()
droid2.die()

Robot.how_many()