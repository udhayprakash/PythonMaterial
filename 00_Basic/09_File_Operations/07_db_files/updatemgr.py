#!/usr/bin/env python

import sys
import gadfly.dbapi20

connection = gadfly.dbapi20.connect('pydb', 'db')

cursor = connection.cursor()

newmgr   = sys.argv[2]
employee = sys.argv[1]

# Query to find the employee ID.
query = """
select e.empid
from user u, employee e 
where username=? and u.employeeid = e.empid
"""

cursor.execute(query,(newmgr,));
for row in cursor.fetchone(): 
    if (row != None):
        mgrid = row

# Note how we use the same query, but with a different name.
cursor.execute(query,(employee,));
for row in cursor.fetchone(): 
    if (row != None):
        empid = row

# Now, modify the employee.
cursor.execute("update employee set manager=? where empid=?", (mgrid,empid))

connection.commit()
cursor.close()
connection.close()
