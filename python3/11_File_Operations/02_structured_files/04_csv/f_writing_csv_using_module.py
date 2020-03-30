#!/usr/bin/python
"""
Purpose: Writing csv using csv module

"""
import csv
with open('other_file.csv', 'w', newline='') as gh:
    header_names = ('sno', 'name', 'age', 'designation')
    writer = csv.DictWriter(gh, delimiter=',', fieldnames=header_names)

    # To write the headers
    writer.writeheader()

    print(dir(writer))
    writer.writerow({
        'sno': 1,
        'name': 'akhila',
        'age': 11,
        'designation': 'carpenter'
    })
    writer.writerows([
        {
            'sno': 2,
            'name': 'hiral',
            'age': 12,
            'designation': 'software'
        },
        {
            'sno': 3,
            'name': 'neha',
            'age': 13,
            'designation': 'business'
        }
    ])
    gh.close()