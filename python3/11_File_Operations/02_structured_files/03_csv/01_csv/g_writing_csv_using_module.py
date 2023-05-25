#!/usr/bin/python
"""
Purpose: Writing csv using csv module

"""
import csv

with open("third.csv", mode="w") as fh:
    header_names = ("sno", "name", "age", "designation")

    writer = csv.writer(fh, delimiter=",")

    writer.writerow(header_names)

    # To write a single record
    writer.writerow([1, "akhila", 11, "carpenter"])

    # To write multiple records
    writer.writerows(
        [
            [2, "neha", 13, "business"],
            [3, "hiral", 12, "software"],
            [4, "", 12, "software"],
            [5, "", 0, "software"],
        ]
    )
