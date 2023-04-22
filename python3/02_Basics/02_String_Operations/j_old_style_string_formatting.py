#!/usr/bin/python3
"""
Purpose: String Formatting
            - Types
                1. Old Style formatting (or literal formatting)
                2. New Style formatting
                3. F-Strings  ( works from python 3.6+)

OLD-Style formatting
    %d - integer
    %i - integer

    %c - single char
    %s - string/char

    %f - floating-point
    %F - floating-point

    %o - octal
    %x - hexadecimal lowercase
    %X - hexadecimal uppercase

"""
print("" % ())
print("My lucky number is %d")
print("My lucky number is %d" % (12))
print("My lucky number is %d" % 12)
print("My lucky number is %d" % 12.34)  # int(12.34)

# print('My lucky number is %d' % '12')
# TypeError: %d format: a number is required, not str


print()
print("My lucky number is %s" % "12")
print("My lucky number is %f" % 12.34)
print("My lucky number is %f" % 12)  # float(12)
print("My lucky number is %f" % False)

print()  # str()
print("My lucky number is %s" % True)
print("My lucky number is %s" % None)
print("My lucky number is %s" % 1)
print("My lucky number is %s" % 13.4)
print("My lucky number is %s" % 133224234)
print("My lucky number is %s" % "python")

print()  # repr()
print("My lucky number is %r" % True)
print("My lucky number is %r" % None)
print("My lucky number is %r" % 1)
print("My lucky number is %r" % 13.4)
print("My lucky number is %r" % 133224234)
print("My lucky number is %r" % "python")


print()
# %o - octal
print("%o" % 34, oct(34))
# %x - hexadecimal lowercase
print("%x" % 34, hex(34))
# %X - hexadecimal uppercase
print("%X" % 34, hex(34))
# %b - binary
# print('%b' % (12), bin(12))
# ValueError: unsupported format character 'b' (0x62) at index 1


print()
print("%s" % "12")
print("%c" % "1")
print("%s" % "1")


print()  # float()  -- 6 digits post decimal
print("%f" % 12.34)  # 12.340000
print("%F" % 12.34)  # 12.340000
print("%F" % 12.34223123123123)  # 12.342231

print()
print("%g" % 12.34)  # 12.34
print("%G" % 12.34)  # 12.34
print("%G" % 12.34223123123123)  # 12.3422

print()
print("%e" % 12.34)  # 1.234000e+01
print("%E" % 12.34)  # 1.234000E+01
print("%E" % 12.34223123123123)  # 1.234223E+01

print()

import math

print(math.pi)  # 3.141592653589793
print("%d" % math.pi)  # 3
print("%f" % math.pi)  # 3.141593
print("%9f" % math.pi)  #  3.141593
print("%9.3f" % math.pi)  #     3.142

###################################################
print()
print("lucky My lucky number is %d only." % 786)
print("pi value is %f!!!!!!!!!!" % 3.1416)
print("pi value is %10f!!!!!!!!!!" % 3.1416)
print("pi value is %10.3f!!!!!!!!!!" % 3.1416)
print("pi value is %010.3f!!!!!!!!!!" % 3.1416)

print("my name is %s - %s." % ("Udhay", "Prakash"))
print()

print("My name is %s. I am %d old paying a tax of %f")
print("My name is %s. I am %d old paying a tax of %f" % ("Udhay", 99, 15.5))

# print('My name is %s. I am %d old paying a tax of %f' % ('Udhay', '99', 15.5))
# TypeError: %d format: a number is required, not str

print()
print("My name is %r. I am %r old paying a tax of %r" % ("Udhay", "78", 15.5))
print("My name is %s. I am %s old paying a tax of %s" % ("Udhay", "78", 15.5))

# print('My name is %s. I am %s old paying a tax of %s' % ('Udhay', 15.5))
# TypeError: not enough arguments for format string

print(
    "%(language)s has %(My lucky number)03d quote types."
    % {"language": "Python", "My lucky number": 2}
)

print()
print("2".zfill(3))  # '002'
print("%03d" % 2)  # '002'
print("%3d" % 2)  # '  2'


# Limitations of old style string formatting
# 1. same data types need to be passed
# 2. If same value need to go more than one time,
#     those many number of times, values need to be passed
