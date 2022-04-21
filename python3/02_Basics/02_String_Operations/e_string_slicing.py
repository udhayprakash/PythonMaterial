#!/usr/bin/python3
"""
Purpose: String slicing operations
"""
language = "Python Programming"

# P   y  t  h  o n   P r o g  r  a  m  m  i  n  g
# 0   1  2  3  4 5 6 7 8 9 10 11 12 13 14 15 16 17   - forward indexing
# -18                                    -3 -2 -1    - reverse indexing


# String Slicing [start_index:final_index, step]
# default start_index = 0
# default final_index = string length
# default step = +1

# language[0:7:+1] => 0, 1, 2, 3, 4, 5, 6
print("language[:7]  :", language[:7])
print("language[0:]  :", language[0:])  # language[0:18:+1]
print("language[6:]  :", language[6:])  # language[6:18:+1]
print()

print("language[:]   :", language[:])  # language[0:18:+1]
print("language      :", language)
print("language[::]  :", language[::])  # default step = +1=> language[0:18:+1]
print()

print("language[::1] :", language[::1])  # language[0:18:+1]
print("language[::3] :", language[::3])  # language[0:18:+3]
print()

# If step is -ve, and start_index and final_index were not given,
# then
#   start_index = length of string - 1
#   final_index = -1
# str reversal  language[17:-1:-1]=> 17,16,15, .... 3, 2, 1, 0
print("language[::-1] :", language[::-1])
print("language[::-2] :", language[::-2])  # str reversal  language[17:-1:-2]
# str reversal  language[17:-1:-5]=> 17,12,7,2
print("language[::-5] :", language[::-5])
print()


# example
name = "Varun Dhawan"

#   V  a    r    u   n     D  h  a  w  a  n
#   0  1    2    3   4  5  6  7  8  9  10 11 - forward indexing
# -12  -11 -10  -9  -8 -7 -6 -5 -4 -3 -2 -1  - reverse indexing

print("name             :", name)
print("name[:]          :", name[:])
print("name[::]         :", name[::])
print("name[::1]        :", name[::1])
print("name[::-1]       :", name[::-1])  # string reversal

# Assignment: reverse each word in given sentence in same order
# input : today is good day
# output: yadot si doog yad

# positive indexing
print("name[4:]            :", name[4:])  # name[4:12:+1]
print("name[:4]            :", name[:4])
print("name[:5]            :", name[:5])
print()

# Reverse indexing - get last 6 characters
print("name[:-6]           :", name[:-6])

print("name[-6:]           :", name[-6:])
print("name[len(name)-6:]  :", name[len(name) - 6 :])
print()

print("name[2:-5]          :", name[2:-5])  # name[2:7:+1]
# NOTE: not recommended to use a combination of both pos and neg indices
