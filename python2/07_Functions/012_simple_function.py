#!/usr/bin/python
"""
Purpose: Functions Demo

   Scope - Global and local
"""
alphabets = {'a':1, 'b':2} # mutable object


def computation():
    print 'in - before - alphabets', alphabets
    alphabets['c'] = 3
    print 'in - after - alphabets', alphabets


computation()
print 'outside --- alphabets', alphabets
