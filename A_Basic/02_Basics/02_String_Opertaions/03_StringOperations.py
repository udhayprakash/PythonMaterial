#!/usr/bin/python
"""
Purpose: Demonstration of String Operations
"""

language = 'Python Programming'
print 'language       = ', language
print 'type(language) = ', type(language)

print 'STRING OPERATIONS'
print '--------------------------------------'
print 'string Indexing'

print 'len(language):', len(language)

# P   y  t  h  o n   P r o g  r  a  m  m  i  n  g
# 0   1  2  3  4 5 6 7 8 9 10 11 12 13 14 15 16 17   - forward indexing
# -18                                    -3 -2 -1    - reverse indexing
#

print 'language[0] :', language[0]
print 'language[14]:', language[14]
print 'language[6] :', language[6]
print 'language[17] :', language[17]
# print 'language[18] :', language[18] # IndexError

print
print 'language[-0] :', language[-0]
print 'language[-3] :', language[-3]

print 'language[-18] :', language[-18]
# print 'language[-19] :', language[-19]  # IndexError

print '------------------------------'
print 'String Slicing'

# P   y  t  h  o n   P r o g  r  a  m  m  i  n  g
# 0   1  2  3  4 5 6 7 8 9 10 11 12 13 14 15 16 17   - forward indexing
# -18                                    -3 -2 -1    - reverse indexing
#-0]
print 'language       :', language
print 'language[0:11] :', language[0:11]
print 'language[5:17] :', language[5:17]
print 'language[7:10] :', language[7:10]
# In python, it doesn't include the last value
print 'language[0:5]  :', language[0:5]
print 'language[0:6]  :', language[0:6]

print 'language[7:18] :', language[7:18]
print 'language[7:999]:', language[7:999]  # 999 index isn't present
print 'language[45:87]:', language[45:87]  # indexes are not present

# string slicing - string[start_index: final_index: step]
# Default - step = +1
print
print "language[7:18]   =", language[7:18]
print "language[7:18:1] =", language[7:18:1]
print "language[7:18:3] =", language[7:18:3]
print "language[7:18:-1]=", language[7:18:-1]  # 7-1 = 6 ; it is not between 7 and 18

print 'language[18:7:-1]', language[18:7:-1]  # 18-1 = 17
print 'language[18:7:-3]', language[18:7:-3]  # 18-3 = 15
#         18 15 12 9 
#            i   a o
#         17 14 11 8
#         g  m  r  r

print
# default start_index = 0
# default final_index = last index of string + 1
print 'language[:7] :', language[:7]  # equal to language[0:7:+1]
print 'language[0:] :', language[0:]  # equal to language[0:18:+1]
print 'language[6:] :', language[6:]  # equal to language[6:18:+1]
print
print 'language[:]  :', language[:]  # equal to language[0:18:+1]
print language

print 'language[::] :', language[::]  # default step = +1
print 'language[::1] :', language[::1]
print 'language[::3] :', language[::3] # equal to language[0:18:+3]
print
# If step is -ve, and start_index and final_index were not given,
# then start_index = last string index and
# final_index = -1
print 'language[::-1] :', language[::-1]  # string reversal
print 'language[::-2] :', language[::-2]  # string reversal
print 'language[::-5] :', language[::-5]  # string reversal
