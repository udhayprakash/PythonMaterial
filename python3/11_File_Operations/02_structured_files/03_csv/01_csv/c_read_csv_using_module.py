"""
Purpose: Reading(Parsing) CSV using csv module
"""
import csv

# print(dir(csv))

# for each_attribute in dir(csv):
#     if each_attribute.startswith('__'):
#         continue
#     print(each_attribute)


with open("first.csv", mode="r") as fh:
    # fh.read()
    file_Content = csv.reader(fh, delimiter=",")
    # print(file_Content)
    # print(list(file_Content))

    # To skip the header
    next(file_Content, None)

    names = []
    for each_line in file_Content:
        # print(each_line)
        name = each_line[1]
        names.append(name)

print(f"{names =}")
