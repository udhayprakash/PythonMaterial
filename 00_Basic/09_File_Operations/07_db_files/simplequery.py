#!/usr/bin/env python

import gadfly.dbapi20

connection = gadfly.dbapi20.connect('pydb', 'db')

cursor = connection.cursor()

cursor.execute("""
select employee.firstname, employee.lastname, department.name 
from employee, department
where employee.dept = department.departmentid
order by employee.lastname desc
""")

for row in cursor.fetchall(): 
    print row

cursor.close()
connection.close()
