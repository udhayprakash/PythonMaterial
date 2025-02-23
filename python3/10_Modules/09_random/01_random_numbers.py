#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import secrets

"""
Purpose: Demonstration of random module

    Python random module, uses pseudo-random generator (PRNG)
    called the Mersenne Twister.

NOTE: random module is good enough for many purposes, including simulations,
numerical analysis, and games, but it's definitely not good enough for
cryptographic use.
In Python3, 'secret' module is used for cryptographic purpose.
"""
# Generate a pseudo-random number between 0 and 1.
print("random.random()      :", secrets.SystemRandom().random())

# Generate a large pseudo-random number
print("random.random() * 100:", secrets.SystemRandom().random() * 100)
print("random.random() * 100:", secrets.SystemRandom().random() * 100)

# if we set the seed, we guarantee that we will get the same answer
secrets.SystemRandom().seed(18485)
# NOTE: only supported seed types are: None,int, float, str, bytes, and bytearray.

print(secrets.SystemRandom().random())  # should give 0.6797936184081204
print(secrets.SystemRandom().random())  # should give 0.9122712611873796
print(secrets.SystemRandom().random())  # should give 0.12926723301605425

secrets.SystemRandom().seed("slartibartfast")
s = [secrets.SystemRandom().random() for i in range(3)]
print(s)  # should give [0.7725766895236029, 0.850635131875668, 0.11481894112205038]
print()

print("os.urandom(1024)", os.urandom(1024))
secrets.SystemRandom().seed(os.urandom(1024))

print(secrets.SystemRandom().random())  # should give 0.7819713562511514
print(secrets.SystemRandom().random())  # should give 0.4669615948613485
print(secrets.SystemRandom().random())  # should give 0.6987920562874854
