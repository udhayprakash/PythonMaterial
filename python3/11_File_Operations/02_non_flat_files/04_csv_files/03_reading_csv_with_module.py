import csv

# print("dir(csv)", dir(csv))

with open('mydata.csv', 'rt') as csv_fh:
    data = csv.reader(csv_fh, delimiter=',')
    next(data, None)  # skip the headers # data.next()

    print(data, type(data))

    for index, eachline in enumerate(data):
        print(index, '->', eachline)

    # for loopnumber, eachline in enumerate(data):
    #     if not loopnumber:
    #         continue
    #     print("eachline[0]", eachline[0])

    csv_fh.close()
