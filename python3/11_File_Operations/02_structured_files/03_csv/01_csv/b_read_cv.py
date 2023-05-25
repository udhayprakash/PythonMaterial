#!/usr/bin/python
"""
Purpose: Reading(Parsing) csv, using unstructure file ops
"""
# Method 1
with open("first.csv", mode="r") as fh:
    file_content = fh.read()

    names = []
    for each_line in file_content.splitlines()[1:]:
        # print(each_line.split(","))
        name = each_line.split(",")[1]
        names.append(name)

print(f"{names =}")


# Method 2
with open("first.csv", mode="r") as fh:
    file_content = fh.readlines()

    names = []
    for each_line in file_content[1:]:
        # print(each_line.split(","))
        name = each_line.split(",")[1]
        names.append(name)

print(f"{names =}")
