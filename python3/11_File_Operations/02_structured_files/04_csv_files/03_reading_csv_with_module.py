import csv

# print("dir(csv)", dir(csv))

with open('mydata.csv', 'rt') as csv_fh:
    #    data = csv_fh.read()
    data = csv.reader(csv_fh, delimiter=',')
    print(data)

    # TO skip the header 
    next(data, None)

    names = []
    for ech_line in data:
        names.append(ech_line[0])
    print(f'names:{names}')

    csv_fh.flush()
    csv_fh.close()
