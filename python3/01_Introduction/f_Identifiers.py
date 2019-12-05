#!/usr/bin/python

# variable
# 1. keyword
# 2. identifier

import keyword

print(keyword.kwlist)

print(keyword.iskeyword('True'))  # True
print(keyword.iskeyword('true'))  # False
print(keyword.iskeyword('while'))  # True

# Identifier naming conventions
################################
# first character     :  a-z, A-Z, _
# remaining characters:  a-z, A-Z, 0-9, _

# True = 123
# true = 123
# while = 12
# WHILE = 12

name = 'python'
name123 = 'something'
name_soe = 'asdadDF'
name123_two = 'eedasdasdasdsa'
PI = 3.14

# my$name = 'uqwqwqw'# SyntaxError: invalid syntax
# $name = 'uqwqwqw'
# 2name = 'dfdfsdf'

_job = 'farming'
__babu = 'Nagababu'

# OOP - name mangling
# _variable   --> Protected variable
# __variable  --> Private variable

# __variable__  --> Builtin functions
#   Ex: __main__, __init__, __file__

# PYTHON IS CASE-SENSITIVE
###########################

animal = 'cow'
Animal = 'Dog'

# print(ANIMAL) #NameError: name 'ANIMAL' is not defined

# variable casing
#################

# snake casing or underscore casing
cost_of_mangos = 34
cost_of_apples = 12

output_of_sensor = 'asdd'
No_of_processes_running = 123

# camel casing
costOfMangos = 34
costOfApples = 12
outputOfSensor = 'asdd'
NoOfProcesesRunning = 123
# https://ieeexplore.ieee.org/document/5521745?tp=&arnumber=5521745

'''
PEP (python Enhancement Proposal) 8 - coding style guide 
 - class names should be camelCase
 - identifier names should be in snake case .
'''
