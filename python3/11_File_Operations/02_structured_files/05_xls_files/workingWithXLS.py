#!/usr/bin/python

# workingWithXLS.py

try:
    import xlrd
except ImportError as ie:
    print
    ie
    import os

    if not os.system('pip install xlrd'):
        print
        'Unable to install the module!'

try:
    workbook = xlrd.open_workbook('new.xls', 'ab+')
    worksheet = workbook.sheet_by_name('sheet1')
    numRow = worksheet.nrows - 1
    currRow = -1
    while currRow < numRow:
        currRow += 1
        row = worksheet.row(currRow)
        print(row)
except IOError as io:
    print(io)
    print("Please ensure that the specified file is present in the current working directory")
except Exception, ex:
    print(ex)
    
