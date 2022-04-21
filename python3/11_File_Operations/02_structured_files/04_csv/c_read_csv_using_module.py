#!/usr/bin/python
"""
Purpose: Reading(Parsing) CSV using csv module
"""
import csv

# for each_attribute in dir(csv):
#     if each_attribute.startswith('__'):
#         pass
#     print(each_attribute)


with open("my_file.csv", "r") as fh:
    file_content = csv.reader(fh, delimiter=",")
    # print(file_content)

    # To skip the header
    next(file_content, None)

    names = []
    for each_line in file_content:
        name = each_line[1]
        names.append(name)
    fh.close()

print(f"{names=}")
