#!/usr/bin/python
"""
Purpose: Writing non-english characters

"""
import csv

with open("non_english.csv", "w", newline="", encoding="utf-8") as gh:
    header_names = ("sno", "name", "language")
    writer = csv.writer(gh, delimiter=",")

    # To write the headers
    writer.writerow(header_names)

    writer.writerow([1, "english", "Python"])
    writer.writerows(
        [
            [2, "Russian", "питон"],
            [3, "Italian", "Pitone"],
            [4, "Japanese", "パイソン"],
            [5, "Chinese", "蟒蛇"],
            [6, "Telugu", "పైథాన్"],
            [7, "Tamil", "பைதான்"],
            [8, "Hindi", "अजगर"],
        ]
    )
    gh.close()
