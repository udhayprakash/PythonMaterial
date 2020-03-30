#!/usr/bin/python
"""
Purpose: Reading(Parsing) CSV using csv module
"""
import csv

# for each_attribute in dir(csv):
#     print(each_attribute)

with open('my_file.csv', 'r') as fh:
    file_content = csv.reader(fh, delimiter=',')
    # print(file_content)

    # To skip the header
    next(file_content, None)

    names = []
    for each_line in file_content:
        # print(each_line)
        names.append(each_line[1])
    fh.close()

print(names)
