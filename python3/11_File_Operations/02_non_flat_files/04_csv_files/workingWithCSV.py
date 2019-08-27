#!/usr/bin/python
# workingWithCSV.py
import csv
'''
    Purpose : Working with CSV files

'''
# with is called as a context manager
with open('sampleCSVFile.csv') as csvFile:
    data = csv.reader(csvFile, delimiter = ',')
    print(data)  # it is an iterator object
    for row in data:
        #print row
        print row[0]

    csvFile.close()

# Assignment 3: write a function to display all the cars, in the sampleCSVFile.csv
