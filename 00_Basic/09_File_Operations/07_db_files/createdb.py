#!/usr/bin/env python

import os
import gadfly
connection = gadfly.gadfly()

os.mkdir('db')

connection.startup('pydb', 'db')

cursor = connection.cursor()


# Create tables.
cursor.execute("""
create table employee 
    (empid integer, 
    firstname varchar, 
    lastname varchar, 
    dept integer,
    manager integer,
    phone varchar)
""")

cursor.execute("""
create table department 
    (departmentid integer, 
    name varchar, 
    manager integer)
""")

cursor.execute("""
create table user 
    (userid integer, 
    username varchar, 
    employeeid integer)
""")

# Create indices.
cursor.execute("""create index userid on user (userid)""")
cursor.execute("""create index empid on employee (empid)""")
cursor.execute("""create index deptid on department (departmentid)""")
cursor.execute("""create index deptfk on employee (dept)""")
cursor.execute("""create index mgr on employee (manager)""")
cursor.execute("""create index emplid on user (employeeid)""")
cursor.execute("""create index deptmgr on department (manager)""")


connection.commit()
cursor.close()

connection.close()
