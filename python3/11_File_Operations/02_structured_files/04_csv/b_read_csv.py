#!/usr/bin/python
"""
Purpose: Reading(Parsing) csv, using unstructure file ops
"""
with open('my_file.csv', 'r') as fh:
    file_content = fh.readlines()
    # print(type(file_content))
    # print(file_content)
    names = []
    for each_line in file_content[1:]:
        # print(type(each_line), each_line)
        each_line_content = each_line.strip().split(',')
        names.append(each_line_content[1])
    fh.close()

print(names)