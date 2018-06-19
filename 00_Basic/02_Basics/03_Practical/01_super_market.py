#!/usr/bin/python
"""
Purpose: Super Market Application

Products:
    mangos
    Apples

Price:
    mangos  5/- per piece
    apples  15/- per piece

discount = 20%

User will buy 3 dozen mangos and 8 dozen apples
"""
__author__ = 'Python Tutor'

DOZEN = 12
# DISCOUNT = 20/100      # type-casting int/int = int
DISCOUNT = 20 / 100.0

cost_of_mango = 5
cost_of_apple = 15

qty_of_mangos = 3 * DOZEN
qty_of_apples = 8 * DOZEN

Total_cost_price = (cost_of_mango * qty_of_mangos) + (cost_of_apple * qty_of_apples)  # PEDMAS

print 'Total cost Price is', Total_cost_price

billable_amount = Total_cost_price - (Total_cost_price * DISCOUNT)

print 'Billable Amount is', billable_amount
