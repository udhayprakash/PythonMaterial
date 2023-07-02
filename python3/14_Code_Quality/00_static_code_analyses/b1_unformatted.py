# Unused import
import os
# Enforcing consistent import order
import sys

# Detecting unused variables


def my_function():
    unused_variable = 10


# Enforcing naming conventions
invalid_variable = 10
# Detecting unused function arguments


def my_function(arg1, arg2):
    return arg1
# Identifying missing docstrings


def my_function():
    pass


# Enforcing line length limit
long_line = "This is a very long line that exceeds the line length limit defined by Pylint"
# Identifying unused class methods


class MyClass:
    def unused_method(self):
        pass
# Detecting unreachable code


def my_function():
    return 10
    print("This code is unreachable")
# Identifying missing return statements in functions/methods


def my_function():
    pass


# Enforcing consistent whitespace usage
invalid_whitespace = 10 + 5

# Identifying incorrect use of mutable default function arguments


def my_function(arg=[]):
    arg.append(10)


# Checking for inconsistent use of quotation marks
invalid_string = 'This string uses single quotes instead of double quotes'

# Detecting unnecessary pass statements
try:
    1 / 0
except Exception as ex:
    print(ex)
    pass

# Identifying incorrect variable reassignment
variable = 10
variable = "updated value"

"""
pylint can only list the problems, but not rectify themStop.

autopep8 can help to auto format


python b1_unformatted.py
python -m autopep8 b1_unformatted.py   
python -m autopep8 -d b1_unformatted.py

cp b1_unformatted.py b0_unformatted.py.bak
python -m autopep8 -i b1_unformatted.py


TO update changes on same file
    autopep8 --in-place --aggressive --aggressive <filename>

To create backup and to changes
    cp b1_unformatted.py b1_unformatted.py.bak && autopep8 --aggressive --in-place b2_formatted.py


"""
