import csv

# print("dir(csv)", dir(csv))

with open('mydata.csv', 'rt') as csv_fh:
    data = csv.DictReader(csv_fh, delimiter=',')

    print(data, type(data))

    names = []
    for each_line in data:
        names.append(each_line['Name'])

    print(names)
    csv_fh.close()
