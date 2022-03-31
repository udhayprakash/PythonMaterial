#!/usr/bin/python3
"""
Purpose: importance of thread locks for synchonization

NOTE: The code between the acquire() and release() methods are
 executed atomically so that there is no chance that a thread will 
 read a non-updated version after another thread has already made a change.

"""
import threading

# Declraing a lock
lock = threading.Lock()
deposit = 100


def add_profit():
    """ Function to add profit to the deposit"""
    global deposit
    for i in range(100000):
        lock.acquire()
        deposit = deposit + 10
        lock.release()


def pay_bill():
    """ Function to deduct money from the deposit"""
    global deposit
    for i in range(100000):
        lock.acquire()
        deposit = deposit - 10
        lock.release()


# Creating threads
thread1 = threading.Thread(target=add_profit, args=())
thread2 = threading.Thread(target=pay_bill, args=())

# Starting the threads
thread1.start()
thread2.start()

# Waiting for both the threads to finish executing
thread1.join()
thread2.join()

# Displaying the final value of the deposit
print(deposit)
