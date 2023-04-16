#!/usr/bin/python3
"""
Purpose: Identifiers in Python

    Variable
        1. keyword   --> words which have some meaning in that language
        2. Identifier -> words which are defined by user(developers)

"""
# Loading a module
import keyword

print(keyword.kwlist)
# ['False', 'None', 'True', 'and', 'as', 'assert', 'async',
# 'await', 'break', 'class', 'continue', 'def', 'del', 'elif',
# 'else', 'except', 'finally', 'for', 'from', 'global', 'if',
#  'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or',
#  'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']


print(True)  # True
# print(true) NameError: name 'true' is not defined. Did you mean: 'True'?


my_value = "something"
print(my_value)  # Identifier

# True = 'something'
# SyntaxError: cannot assign to True

print(keyword.iskeyword("True"))  # True
print(keyword.iskeyword("true"))  # False
print(keyword.iskeyword("my_value"))  # False


# ------------------------------------------------------
# Identifiers - User-defined variables
#   - Naming Convention
#      1. keywords should not be used as identifiers
#      2. first character: a-z, A-Z, _
#      3. remaining chars: a-z, A-Z, _, 0-9

# ---- Rule 1
# True = 123  # SyntaxError: cannot assign to True
# None = 'Nothing'  # SyntaxError: cannot assign to None

# PEP 8 - Dont create identifiers which are similar as Keywords
true = 123
none = "Nothing"

true_value = 123
none_result = "Nothing"

# ---- Rule 2 & 3
name = "Priyanka"
name_of_student = "Priyanka"
first_name = "Priyanka"
student_1 = "Priyanka"
class_02_a = "Python comment operations"
first_____child = "Satvik"


# PEP 8 recommends to use capitals for constants
PI = 3.1416
DOZEN = 12

# $name = "Priyanka"
# name-of-student = "Priyanka"
# name of student = "Priyanka"
# 1st_name = "Priyanka"  SyntaxError: invalid decimal literal

_2nd_student = "someone"

_job = "software development"
__role = "Product support"
___salary = 1231231232312323233


# OOP -> name mangling
# variable   -> Public variable
# _variable  -> Protected variable
# __variable -> Private variable

# __variable__ ->  Built-in functions
# Ex: __file__, __name__, __doc__, __dict__, __init__

print("__name__ =", __name__)  # __main__
print("__file__ =", __file__)

# print('__pavithra__ =', __pavithra__)
# NameError: name '__pavithra__' is not defined
