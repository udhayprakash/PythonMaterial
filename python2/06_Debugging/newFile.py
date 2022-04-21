#!/usr/bin/python

__author__ = 'udhay'

costOfMangos = float(raw_input('Enter the cost of Mangos, in Euros: '))

def grocerryShop(quantity):
    costOfApples = 2

    TotalCost = quantity*(costOfApples + costOfMangos)
    return TotalCost

print grocerryShop(12)
