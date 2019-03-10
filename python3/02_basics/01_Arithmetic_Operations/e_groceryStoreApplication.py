#!/usr/bin/python
"""
Purpose: Grocery Store Demonstration

Products: Apples and Mangos
quantity in dozens

"""
DOZEN = 12

costOfApples = 12
costOfMangos = 5

quantityInDozensOfApples = 3
quantityInDozensOfMangos = 7
# PEMDAS rule
TotalCost = costOfApples * (quantityInDozensOfApples * DOZEN) + \
            costOfMangos * quantityInDozensOfMangos * DOZEN  # left to right and top to bottom
print("Total Cost = ", TotalCost )


