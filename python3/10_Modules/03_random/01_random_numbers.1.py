#!/usr/bin/python
# -*- coding: utf-8 -*-
import random
import os
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
print('random.random()', random.random())

# Generate a large pseudo-random number
print('random.random() * 100', random.random() * 100)

# if we set the seed, we guarantee that we will
# get the same answer
random.seed(18485)
print((random.random()))  # should give 0.6797936184081204
print((random.random()))  # should give 0.9122712611873796
print((random.random()))  # should give 0.12926723301605425

random.seed('slartibartfast')
s = [random.random() for i in range(3)]
print(s)  # should give [0.7725766895236029, 0.850635131875668, 0.11481894112205038]
print()

print('os.urandom(1024)', os.urandom(1024))
random.seed(os.urandom(1024))
print((random.random()))  # should give 0.7819713562511514
print((random.random()))  # should give 0.4669615948613485
print((random.random()))  # should give 0.6987920562874854
