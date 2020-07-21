#!/usr/bin/python
"""
Purpose: Reading(Parsing) csv, using unstructure file ops
"""
# Method 1
with open('my_file.csv', 'r') as fh:
    file_content = fh.read()
    # print(file_content.splitlines())
    names = []
    for each_line in file_content.splitlines()[1:]:
        # print(each_line.split(','))
        name = each_line.split(',')[1]
        names.append(name)

    fh.close()

print(f'{names =}')

# Method 2
with open('my_file.csv', 'r') as fh:
    file_content = fh.readlines()
    # print(file_content)
    names = []
    for each_line in file_content[1:]:
        # print(each_line.split(','))
        name = each_line.split(',')[1]
        names.append(name)

    fh.close()

print(f'{names =}')