#!/usr/bin/python

__author__ = 'python tutor'

import csv
for i in range(12):
    print i+1,

with open('sampleCSVFile.csv') as csvFile1:
    data = csv.reader(csvFile1, delimiter=',')

    print '\n', data

    vegetables = fruits = cars = []     #It will result in all these objects will point to the same location
    #vegetables = []
    #fruits = []
    #cars = []

    # for i in dir(data):
    #    print i,

    for index, row in enumerate(data):
        if index == 0:
            continue  # to skip first iteration
        fruits.insert(index, row[0])
        # print fruits
        vegetables.insert(index, row[1])
        cars.insert(index, row[2])

        # print row, type(row)
        # print row[0], type(row[0])
        # fruits.append(row[0])
        # print fruits.append(row[0])
        # print vegetables.append(row[1])
        # print cars.append(row[2])

    print '-' * 50
    print 'fruits :', fruits
    print 'vegetables', vegetables
    print 'cars : ', cars

    print id(fruits), id(vegetables), id(cars)
    csvFile1.close()

