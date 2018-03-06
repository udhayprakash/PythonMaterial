#!/usr/bin/python
"""
Purpose: Super Market Application with user input

Products:
    dall
    rice

Price:
    dall  7/- per kg
    rice  13/- per kg

discount = 13%

User will give in run time
"""
__author__ = 'Python Tutor'

DISCOUNT = 13/100.0  # int/float = float

costOfDall = 7
costOfRice = 13


qtyOfDall = input('Enter the qty of Dall in Kgs:')
print 'qtyOfDall', qtyOfDall
print 'type(qtyOfDall)', type(qtyOfDall)

qtyOfRice = input('Enter the qty of Rice in Kgs:')
print 'qtyOfRice', qtyOfRice
print 'type(qtyOfRice)', type(qtyOfRice)


# \ is a line continuation character
totalCostPrice = (costOfDall * qtyOfDall) + \
                            (costOfRice * qtyOfRice)


print 'Total cost Price is', totalCostPrice

billableAmount = (totalCostPrice
                 - totalCostPrice * DISCOUNT)

print 'Billable Amount is', billableAmount



# input() is not recommended due to security issue

