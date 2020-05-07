#!/usr/bin/python
"""
Purpose: Reading(Parsing) csv using pandas module
"""
import pandas

# print(dir(pandas))

# Loading a csv
data_frame = pandas.read_csv('my_file.csv')

print(type(data_frame))
print(data_frame)
print()

print(list(data_frame.name))