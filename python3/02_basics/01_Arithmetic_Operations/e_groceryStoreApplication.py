#!/usr/bin/python
"""
Purpose: Fruits Store Demonstration

Products: Apples and Mangos
quantity in dozens

"""
DOZEN = 12

# cost is per piece 
costOfApple = 12
costOfMangos = 5

quantityInDozensOfApples = 3
quantityInDozensOfMangos = 7

# PEMDAS rule
TotalCost = costOfApple * (quantityInDozensOfApples * DOZEN) + \
                costOfMangos * quantityInDozensOfMangos * DOZEN  # top to bottom and left to right 
print("Total Cost = ", TotalCost )

