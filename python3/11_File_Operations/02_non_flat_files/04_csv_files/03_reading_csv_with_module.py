import csv

# print("dir(csv)", dir(csv))

with open('mydata.csv', 'rt') as csv_fh:
    data = csv.reader(csv_fh, delimiter=',')
    next(data, None)  # skip the headers # data.next()

    print(data, type(data))

    names = []
    for each_line in data:
        names.append(each_line[0])

    print(names)
    csv_fh.close()
