#!/usr/bin/python
'''
https://www.hackerrank.com/challenges/python-raw-input
'''

# Enter your code here. Read input from STDIN. Print output to STDOUT
from sys import stdin, stdout

s = stdin.read()  # r"How many chickens does it take to cross the road?")

if 1 <= len(s) <= 500:
    stdout.write(s)
