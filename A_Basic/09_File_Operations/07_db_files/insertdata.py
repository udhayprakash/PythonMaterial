#!/usr/bin/env python

import gadfly.dbapi20

connection = gadfly.dbapi20.connect('pydb', 'db')

cursor = connection.cursor()

# Create employees.
cursor.execute("""
insert into employee (empid,firstname,lastname,manager,dept,phone) 
values (1,'Eric','Foster-Johnson',1,1,'555-5555')""")

cursor.execute("""
insert into employee (empid,firstname,lastname,manager,dept,phone) 
values (2,'Peter','Tosh',2,3,'555-5554')""")

cursor.execute("""
insert into employee (empid,firstname,lastname,manager,dept,phone) 
values (3,'Bunny','Wailer',2,2,'555-5553')""")

# Create departments.
cursor.execute("""
insert into department (departmentid,name,manager) 
values (1,'development',1)""")

cursor.execute("""
insert into department (departmentid,name,manager) 
values (2,'qa',2)""")

cursor.execute("""
insert into department (departmentid,name,manager) 
values (3,'operations',2)""")

# Create users.
cursor.execute("""
insert into user (userid,username,employeeid) 
values (1,'ericfj',1)""")

cursor.execute("""
insert into user (userid,username,employeeid) 
values (2,'tosh',2)""")

cursor.execute("""
insert into user (userid,username,employeeid) 
values (3,'bunny',3)""")

connection.commit()

   
cursor.close()

connection.close()
