#!/usr/bin/python

'''
Purpose: creating a new CSV file

with - context manager

garbage collector -- java, python , ..
    - cpu clock cycle

'''

with open('sampleCSVFile.csv', 'wb') as myCsv:
    # csv header
    myCsv.write('fruits, vegetables, cars\n')
    # csv body
    myCsv.write('Apple, Cabbagge, Benz\n')
    myCsv.write('Mango, Cucumber, Volvo\n')
    myCsv.write('Banana, Raddish, Maruthi suzuki\n')
    myCsv.close()
