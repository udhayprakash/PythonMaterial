#!/usr/bin/python
"""
Purpose: read csv file as done for flat file
"""

with open('sample.csv', 'r') as gh:
    data = gh.readlines()
    # print(data, type(data))

    names = []
    for each_line in data[1:]:
        each_line = each_line.strip()
        names.append(each_line.split(',')[1])

    print(names)
    gh.close()