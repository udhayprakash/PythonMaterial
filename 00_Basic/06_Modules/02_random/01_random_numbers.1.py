#!/usr/bin/python
# -*- coding: utf-8 -*-
import random 
"""
Purpose: demonstration of random module 

    Python random module, uses pseudo-random generator (PRNG) 
    called the Mersenne Twister. 

NOTE: random module is good enough for many purposes, including simulations, 
numerical analysis, and games, but it’s definitely not good enough for 
cryptographic use.
In Python3, 'secret' module is used for cryptographic purpose.
"""
# Generate a pseudo-random number between 0 and 1.
print 'random.random()', random.random()

# Generate a large pseudo-random number
print 'random.random() * 100', random.random() * 100


# if we set the seed, we guarantee that we will
# get the same answer
random.seed(18485)
print random.random() # should give 0.679793618408
print random.random() # should give 0.912271261187
print random.random() # should give 0.129267233016

random.seed('slartibartfast')
s = [random.random() for i in range(3)]
print s   # should give [0.34210536499528865, 0.32598885901995334, 0.8052429197795312]
