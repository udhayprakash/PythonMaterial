#!/usr/bin/python
import logging
__author__ = 'Udhay Prakash'

class Loggable(object):
    """Mixing class to add logging. """

    # Initialize Loggable
    def __init__(self,
                 logFileName = 'log.txt',
                 logLevel = logging.INFO,
                 logName = 'MyApp'):
        self.logFileName = logFileName
        self.logLevel = logLevel
        self.logName = logName
        self.logger = self._get_logger()

    # Creating Logger Object
    def _get_logger(self):
        logger = logging.getLogger(self.logName)
        logger.setLevel(self.logLevel)
        handler = logging.FileHandler(self.logFileName)
        logger.addHandler(handler)
        formatter = logging.Formatter(
            "%(asctime)s: %(name)s - "
            "%(levelname)s - %(message)s")
        handler.setFormatter(formatter)
        return logger

    # Logging methods
    def log(self, logLine, severity = None):
        self.logger.log(severity or self.logLevel, logLine)

    def warn(self, logLine):
        self.logger.warn(logLine)



class MyClass(Loggable):
    """A class that you've written. """

    def __init__(self):
        Loggable.__init__(self, logFileName="log2.txt")
        # super(MyClass, self).__init__(logFileName="log2.txt")

    def doSomeThing(self):
        print "Doing Something!!!"
        self.log("I did something!")
        self.log("Some debugging info", logging.DEBUG)
        self.warn("Something bad happened!")

test = MyClass()
test.doSomeThing()