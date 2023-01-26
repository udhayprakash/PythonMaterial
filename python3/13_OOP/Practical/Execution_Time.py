"""
ExecutionTime

This class is used for timing execution of code.

For example:

    timer = ExecutionTime()
    print 'Hello world!'
    print 'Finished in {} seconds.'.format(timer.duration())

"""

import random
import time


class ExecutionTime:
    def __init__(self):
        self.start_time = time.time()

    def duration(self):
        return time.time() - self.start_time


# ---- run code ---- #


timer = ExecutionTime()
print(dir(timer))
print(callable(timer.start_time))
print(timer.start_time)

sample_list = list()  # []
my_list = [random.randint(1, 888898) for num in range(1, 1000000) if num % 2 == 0]
print("Finished in {} seconds.".format(timer.duration()))
