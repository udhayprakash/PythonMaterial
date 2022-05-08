#!/usr/bin/python3
"""
Purpose: bool() built-in function

    Number  - int & float
    Strings
    None
    boolean
    braces
"""
# bool()
# integer type (int and float)
#       zero     - False
#       non-zero - True
print("bool(12)          ", bool(12))
print("bool(-12)         ", bool(-12))
print("bool(0)           ", bool(0))
print()

print("bool(0.00000000)  ", bool(0.00000000))
print("bool(0.000000001) ", bool(0.000000001))
print("bool(-0.000000001)", bool(-0.000000001))
print()


# strings
#  True - non-empty string
#  False - empty string
print("bool('ball')     ", bool("ball"))
print("bool(' ')        ", bool(" "))  # white-space
print("bool('')         ", bool(""))  # empty string
print()

# None -> False
print("bool(None)       ", bool(None))
print()

# bool - True, False
print("bool(True)       ", bool(True))
print("bool(False)      ", bool(False))
print()

# braces
# [], (), {}
print("(1)              ", bool((1)))
print("(1,)             ", bool((1,)))
print("[1]              ", bool([1]))
print("{1}              ", bool({1}))
print("{1:2}            ", bool({1: 2}))
print()

print("()               ", bool(()))
print("[]               ", bool([]))
print("{}               ", bool({}))
print()


# Relational operations -> Boolean result -> bool()
print("74 > 59           ", 74 > 59)
print("bool(74 > 59)     ", bool(74 > 59))

print("74 <= 59          ", 74 <= 59)
print("bool(74 <= 59)    ", bool(74 <= 59))
print()

# Logical operations -> Boolean result -> bool()
print("1 < 2 and 23 <=23       ", 1 < 2 and 23 <= 23)
#                                  True and  True    = True
print("bool(1 < 2 and 23 <=23) ", bool(1 < 2 and 23 <= 23))
