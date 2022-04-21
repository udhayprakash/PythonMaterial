#!/usr/bin/python
"""
Purpose: demo of bytearray strings
"""

ordinary_string = 'Tomarrow will be ours!!!'
print 'ordinary_string      :', ordinary_string
print 'type(ordinary_string):', type(ordinary_string)

print ordinary_string.find('will be')
print 'ordinary_string[9:17]', ordinary_string[9:17]

# ordinary_string[9:17] = 'is'
# TypeError: 'str' object does not support item assignment

# Ordinary string are immutable
# bytearray strings are mutable

b_string = bytearray('Tomarrow will be ours!!!')
print 'b_string      :', b_string
print 'type(b_string):', type(b_string)

print b_string.find('will be')
print 'b_string[9:17]', b_string[9:17]

b_string[9:17] = 'is '
print 'b_string', b_string

#############################
print
# indexing a bytearray string
print 'ordinary_string[6]', ordinary_string[6]
print 'b_string[6]       ', b_string[6]

print
# ord() and chr()
# Ascii  : o -> 111
print 'chr(111):', chr(111)
print "ord('o'):", ord('o')


# Assignment
# -------------
# caesar cipher
# ------------------  + 3
# A B C D E F
# 0 1 2 3 4 5
# D E F

# bindu
# elqg
