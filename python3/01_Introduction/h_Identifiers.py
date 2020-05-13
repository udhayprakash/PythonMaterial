#!/usr/bin/python
"""
Purpose: Identifiers in Python

    Variable
        1. keyword   --> words which have some meaning in that language
        2. Identifier -> words which are defined by user(developers)
"""
import keyword

print(keyword.kwlist)
# ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 
# 'await', 'break', 'class', 'continue', 'def', 'del', 'elif',
#  'else', 'except', 'finally', 'for', 'from', 'global', 'if', 
#  'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 
#  'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

print(True)      # Keywords

myvalue = 'someyting'
print(myvalue)   # Identifier


print(keyword.iskeyword('True')) # True
print(keyword.iskeyword('true')) # False
print(keyword.iskeyword('myvalue')) # False

# ------------------------------------------------------
# Identifiers - User-defined variables
#   - Naming Convention
#      1. keywords should not be used as identifiers
#      2. first character: a-z, A-Z, _
#      3. remaining chars: a-z, A-Z, _, 0-9

# ---- Rule 1
# True = 123 # SyntaxError: cannot assign to True
# None = 'NOTHING PRESENT' # SyntaxError: cannot assign to None

# PEP 8 - Dont create identifiers which are similar as Keywords
# true = 123

true_value = 123


# ---- Rule 2 & 3
name = 'Chitra'
student_1 = 'Arjun'
class123_ = 123
first___________child = 'Suhan'

PI = 3.1416
DOZEN = 12

# $name = 'somethiing' # SyntaxError: invalid syntax
# first name = 'someting' # SyntaxError: invalid syntax
# first-name = 'someting'  # SyntaxError: cannot assign to operator

first_name = 'Something'
# 2name = 'Johson'  # SyntaxError: invalid syntax
n2ame = 'Johnson'

_job = 'software development'
__role = 'Product support'
___salary = 1231231232312323233

# OOP -> name mangling
# variable   -> Public variable
# _variable  -> Protected variable
# __variable -> Private variable

# __variable__ ->  Built-in functions
# Ex: __file__, __name__, __doc__, __dict__, __init__

print('__name__ =', __name__)
print('__file__ =', __file__)

# print(__chaitra__)  # NameError: name '__chaitra__' is not defined
