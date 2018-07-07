#!/usr/bin/env python

import sys
import gadfly.dbapi20

connection = gadfly.dbapi20.connect('pydb', 'db')

cursor = connection.cursor()

employee = sys.argv[1]

# Query to find the employee ID.
query = """
select e.empid
from user u, employee e 
where username=? and u.employeeid = e.empid
"""
cursor.execute(query,(employee,));
for row in cursor.fetchone(): 
    if (row != None):
        empid = row

# Now, modify the employee.
cursor.execute("delete from employee where empid=?", (empid,))

connection.commit()
cursor.close()
connection.close()
