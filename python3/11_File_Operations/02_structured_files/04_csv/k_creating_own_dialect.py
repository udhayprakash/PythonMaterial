#!/usr/bin/python
"""
Purpose: creating custom dialect

Dialect - https://docs.python.org/3/library/csv.html#dialects-and-formatting-parameters
    - It is a construct that allows you to create, 
    store, and re-use various formatting parameters 
    for your data.

Dialect supports several attributes. The most frequently used are:

   Dialect.delimiter     : Used as the separating character between fields. The default value is a comma (,).
   Dialect.quotechar     : Used to quote fields containing special characters. The default is the double-quote (").
   Dialect.lineterminator: Used to create newlines. The default is '\r\n'.

"""
import csv

csv.register_dialect('myDialect', delimiter='/', quoting=csv.QUOTE_NONE)

with open('other_file3.csv', 'r', newline='') as myFile:
   reader = csv.reader(myFile, dialect='myDialect')
   for row in reader:
       print(row) 


myData = [[1, 2, 3], ['Good Morning', 'Good Evening', 'Good Afternoon']]

csv.register_dialect('myDialect', delimiter='/', quoting=csv.QUOTE_NONE)
with open('quote_none.csv', 'w', newline='') as my_file:
   writer = csv.writer(my_file, dialect='myDialect')
   writer.writerows(myData)


csv.register_dialect('myDialect', delimiter='/', quoting=csv.QUOTE_NONNUMERIC)
with open('quote_nonnumeric.csv', 'w', newline='') as my_file:
   writer = csv.writer(my_file, dialect='myDialect')
   writer.writerows(myData)


csv.register_dialect('myDialect', delimiter='/', quoting=csv.QUOTE_ALL)
with open('quote_all.csv', 'w', newline='') as my_file:
   writer = csv.writer(my_file, dialect='myDialect')
   writer.writerows(myData)


csv.register_dialect('myDialect', delimiter='/', quoting=csv.QUOTE_MINIMAL)
with open('quote_minimal.csv', 'w', newline='') as my_file:
   writer = csv.writer(my_file, dialect='myDialect')
   writer.writerows(myData)