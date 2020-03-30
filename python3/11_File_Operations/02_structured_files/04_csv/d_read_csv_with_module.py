#!/usr/bin/python
"""
Purpose: Reading(Parsing) CSV using csv module
"""
import csv
from pprint import pprint
# for each_attribute in dir(csv):
#     print(each_attribute)

with open('my_file.csv', 'r') as fh:
    file_content = csv.DictReader(fh, delimiter=',')
    # print(file_content)

    # To skip the header
    next(file_content, None)

    names = []
    for each_line in file_content:
        # pprint(each_line)
        # names.append(each_line[1])
        names.append(each_line['name'])
    fh.close()

print(names)
