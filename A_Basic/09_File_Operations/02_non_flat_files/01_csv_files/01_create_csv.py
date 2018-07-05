#!/usr/bin/python

'''
Purpose: creating a new CSV file
'''

with open('sampleCSVFile.csv', 'ab+') as myCsv:
    # csv header
    myCsv.write("fruits, vegetables, cars\n")
    # csv body 
    myCsv.write("Apple, Cabbagge, Benz\n")
    myCsv.write("Mango, Cucumber, Volvo\n")
    myCsv.write("Banana, Raddish, Maruthi suzuki\n")
    myCsv.close()