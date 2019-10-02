#!/usr/bin/python

__author__ = 'udhay'

cost_of_mangos = float(input("Enter the cost of Mangos, in Euros: "))


def grocery_shop(quantity):
    cost_of_apples = 2

    TotalCost = quantity * (cost_of_apples + cost_of_mangos)
    return TotalCost


print(grocery_shop(12))
