import csv

with open('sampleCSVFile.csv') as csvFile:
    readCSV = csv.reader(csvFile, delimiter=',')
    print readCSV
    for row in readCSV:
        print row
        print row[0]
        print row[0], row[1]
    csvFile.close()
    # It is recommended to close the file, after it's use.
    # It deletes that file object.
    # so, file handler can't be used, after its closure.

print '='*80
with open('sampleCSVFile.csv') as csvFile1:
    data = csv.reader(csvFile1, delimiter=',')
    print data
    
    vegetables = []
    fruits = []
    cars = []

    for row in data:
        #cars = row[2]
        (fruits, vegetables, cars) = row
        print fruits, vegetables, cars

    for i in dir(data):
        print i

    csvFile1.close()

print '=' * 80
with open('sampleCSVFile.csv') as c2:
    data2 = csv.reader(c2, delimiter=',')
    print "data is ", data2
    vegetables = []
    fruits = []
    cars = []
    for i, row in enumerate(data2):
        #print i, row
        #print row, type(row)
        fruits.insert(i,row[0])
        print fruits
        #print row[0], type(row[0])
        #fruits.append(row[0])
        #print fruits.append(row[0])
        #print fruits
        # print vegetables.append(row[1])
        # print cars.append(row[2])


    print 'fruits :',fruits
    print 'vegetables', vegetables
    print 'cars : ', cars
    c2.close()