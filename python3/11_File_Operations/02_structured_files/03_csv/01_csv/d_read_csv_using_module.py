"""
Purpose: Reading(Parsing) CSV using csv module
"""
import csv

with open("first.csv", mode="r") as fh:
    # file_Content = csv.reader(fh, delimiter=",")
    file_Content = csv.DictReader(fh, delimiter=",")

    print(file_Content)
    # print(list(file_Content))

    # # To skip the first record  --- NOTE: skipping header
    # next(file_Content, None)

    names = []
    for each_line in file_Content:
        # print(each_line)  # dict
        name = each_line["name"]
        names.append(name)

print(f"{names = }")
