#!/usr/bin/python
"""
Purpose: Reading(Parsing) csv using pandas module
"""
try:
    import pandas
except ModuleNotFoundError as ex:
    print(repr(ex))
    from os import system
    system('pip install pandas --user')
    import pandas

# Loading a csv
data_frame = pandas.read_csv('my_file.csv')

print(type(data_frame))
print(data_frame)

# for each_attribute in dir(data_frame):
#     print(each_attribute)

print(data_frame.name)