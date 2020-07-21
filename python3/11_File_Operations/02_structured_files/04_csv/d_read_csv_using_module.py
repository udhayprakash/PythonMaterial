#!/usr/bin/python
"""
Purpose: Reading(Parsing) CSV using csv module
"""
import csv

with open('my_file.csv', 'r') as fh:
    # file_content = csv.reader(fh, delimiter=',')
    file_content = csv.DictReader(fh, delimiter=',')
    # print(file_content)

    # To skip the first record  --- NOTE: not skipping header
    next(file_content, None)

    names = []
    for each_line in file_content:
        # print(each_line)  # Dict
        name = each_line['name']
        names.append(name)
    fh.close()

print(f'{names =}')