"""
Purpose: Reading(Parsing) CSV using csv module
"""

import csv

# print(dir(csv))

# for each_attribute in dir(csv):
#     if each_attribute.startswith('__'):
#         continue
#     print(each_attribute)

# Method 1 
# fh  = open("my_file.csv", mode="r")

# # fh.read()
# file_content = csv.reader(fh, delimiter=",")
# print(file_content)

# # To skip the header
# next(file_content, None)

# # print(list(file_content))
# names = []
# for eachline in file_content: 
#     # print(eachline[1])
#     names.append(eachline[1])

# print(f"{names =}")
# fh.close()

# Method 2 - using context manager
with open("my_file.csv", mode="r") as fh:

    # fh.read()
    file_content = csv.reader(fh, delimiter=",")
    print(file_content)

    # To skip the header
    next(file_content, None)

    # print(list(file_content))
    names = []
    for eachline in file_content: 
        # print(eachline[1])
        names.append(eachline[1])

    print(f"{names =}")
