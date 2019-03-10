import csv

# names = csv.reader(open('names.csv'))
names = csv.DictReader(open('names.csv'))

for eachline in names:
    # print eachline
    print(eachline)  # .values()
    # print(dict(eachline))  # .values()

