#!/usr/bin/python

# variable
# 1. keyword
# 2. identifier

# Identifier naming conventions
################################
# first character     :  a-z, A-Z, _ 
# remaining characters:  a-z, A-Z, 0-9, _

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
# _variable   --> Private variable
# __variable  --> Protected variable

# __variable__  --> Builtin functions


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

# pascal casing
SalaryOfWorkers = 3000
NoOfProcessesRunning = 123

'''
PEP (python Enhancement Proposal) 8 - coding style guide 
 - class names should be camelcase
 - identifier names should be in snake case .
'''