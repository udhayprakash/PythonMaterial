#!/usr/bin/python
"""
Purpose: Identifier casing 

"""
# Python is case-sensitive language 
animal = 'DOG'
# print(ANIMAL)  # NameError: name 'ANIMAL' is not defined

Animal = 'CAMEL'
ANIMAL = 'Donkey'
print(Animal)      # CAMEL

# variable casing
# 1.snake casing or underscore casing

student = 'Amar'
cost_of_mangos = 12
selling_price_of_apples = 34

output_of_thermal_sensor = 32
no_of_current_processes = 5


# 2. Camel casing 
student = 'Amar'
CostOfMangos = 12 
SellingPriceOfApples = 34

OutputOfThermalSensor = 32
NoOfCurrentProcesses = 5



'''
PEP (python Enhancement Proposal) 8 - coding style guide 
 - class names should be camelCase
 - identifier names should be in snake( or Underscore) case .


Article: https://ieeexplore.ieee.org/document/5521745?tp=&arnumber=5521745

'''