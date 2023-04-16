#!/usr/bin/python3
"""
Purpose: Identifier Casing
    PEP (python Enhancement Proposal) 8 - coding style guide
        - class names should be CamelCase
        - identifier names should be in snake( or Underscore) case .

    Article: https://ieeexplore.ieee.org/document/5521745?tp=&arnumber=5521745

"""
# Python is case-sensitive language
animal = "DOG"
print(animal)

# print(Animal)
# NameError: name 'Animal' is not defined. Did you mean: 'animal'?

ANIMAL = "PIG"
print(ANIMAL)

Animal = "Camel"
print(Animal)

# ------------------------
# variable casing
# 1.snake casing or underscore casing

student = "shiva"
employee_salary = 2343223432.23
cost_of_mango = 12
selling_price_of_apples = 34

output_of_thermal_sensor = 32
no_of_current_processes = 5

# 2. Camel casing
Student = "Shiva"
EmployeeSalary = 2343223432.23
CostOfMango = 12
SellingPriceOfApples = 34

OutputOfThermalSensor = 32
NoOfCurrentProcesses = 5
