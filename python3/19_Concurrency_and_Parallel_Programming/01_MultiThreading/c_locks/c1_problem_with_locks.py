"""
Purpose: Problem with threading.Lock
    program to illustrate the use of Locks
"""


import threading
import time

# creating a Lock object
lock = threading.Lock()

# initializing the shared resource
geek = 0


def sumOne():
    global geek

    # locking the shared resource
    lock.acquire()
    time.sleep(5)
    geek = geek + 1

    # unlocking the shared resource
    lock.release()


def sumTwo():
    global geek

    # locking the shared resource
    lock.acquire()
    geek = geek + 2

    # unlocking the shared resource
    lock.release()


# calling the functions
sumOne()
sumTwo()

# displaying the value of shared resource
print(geek)
