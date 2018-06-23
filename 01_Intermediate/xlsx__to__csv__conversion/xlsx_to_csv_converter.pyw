#!/usr/bin/python
import xlrd
import csv

# open the output csv
with open('sample.csv', 'wb') as myCsvfile:
    # define a writer
    wr = csv.writer(myCsvfile, delimiter="\t")

    # open the xlsx file 
    myfile = xlrd.open_workbook('sample.xlsx')
    # get a sheet
    mysheet = myfile.sheet_by_index(0)

    # write the rows
    for rownum in xrange(mysheet.nrows):
        wr.writerow(mysheet.row_values(rownum))