#!/usr/bin/python
"""
Purpose: Decorator to calculate  the time taken by a function
"""
import time 

def myfuntion():
    total = 0
    for each in range(9999):
        total += each 
    return total 

def time_taken(func):
    def inner(*args, **kwarrgs):
        start_time = time.time()
        # myfuntion() 
        func()
        end_time = time.time()
        time_takem = end_time - start_time
        print(f'It took {time_takem} seconds')
    return inner

result = time_taken(myfuntion)
result()


# syntax sugar 
@time_taken
def myfuntion1():
    total = 0
    for each in range(9999):
        total += each 
    return total 

print(myfuntion1())
