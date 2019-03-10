import csv

names = csv.DictReader(open('names.csv'))

for eachline in names:
    # print eachline
    print eachline  # .values()
