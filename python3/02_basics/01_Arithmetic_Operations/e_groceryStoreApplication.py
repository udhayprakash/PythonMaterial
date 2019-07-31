#!/usr/bin/python
"""
Purpose: Fruits Store Demonstration

Products: Apples and Mangos
quantity in dozens

"""
DOZEN = 12

# Per piece cost
cost_of_mango = 21
cost_of_apple = 32

quantity_of_mangos_in_dozens = 4
quantity_of_apples_in_dozens = 7

total_cost = (quantity_of_apples_in_dozens * DOZEN) * cost_of_apple \
                + (quantity_of_mangos_in_dozens * DOZEN * cost_of_mango)

print('Total Cost = ', total_cost)

# PEMDAS
# Python Execution flow - top-botton & left to right 