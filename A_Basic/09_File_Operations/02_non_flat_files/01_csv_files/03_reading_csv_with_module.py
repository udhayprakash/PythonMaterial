import csv 

print dir(csv)

with open('mydata.csv', 'rb') as csv_fh:
    data = csv.reader(csv_fh, delimiter=',')
    print data, type(data)

    # for index, eachline in enumerate(data):
    #     print index

    for loopnumber, eachline in enumerate(data):
        if not loopnumber:
            continue
        print eachline[0]

    csv_fh.close()