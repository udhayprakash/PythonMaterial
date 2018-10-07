import csv 

print dir(csv)

with open('mydata.csv', 'rb') as csv_fh:
    data = csv.reader(csv_fh, delimiter=',')
    print data, type(data)

    for loopnumber, eachline in enumerate(data[1:]):
        if not loopnumber:
            continue
        print eachline[0]

    csv_fh.close()