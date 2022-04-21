#!/usr/bin/env python

import sqlite3
import sys
from sqlite3 import Error


def create_connection(db_file):
    """create a database connection to a SQLite database"""
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
        sys.exit(1)
    else:
        print(sqlite3.version)
    finally:
        conn.close()


def create_tables(db_file):
    connection = sqlite3.connect(db_file)
    cursor1 = connection.cursor()
    # Create tables.
    cursor1.execute(
        """
        create table if not exists employee
            (empid integer,
            firstname varchar,
            lastname varchar,
            dept integer,
            manager integer,
            phone varchar)
        """
    )
    cursor1.execute(
        """
    create table if not exists department
        (departmentid integer,
        name varchar,
        manager integer)
    """
    )
    cursor1.execute(
        """
    create table if not exists user
        (userid integer,
        username varchar,
        employeeid integer)
    """
    )
    connection.commit()
    cursor1.close()


def create_indexes_for_db(db_file):
    connection = sqlite3.connect(db_file)
    cursor = connection.cursor()
    # Create indices.
    cursor.execute("""create index userid on user (userid)""")
    cursor.execute("""create index empid on employee (empid)""")
    cursor.execute("""create index deptid on department (departmentid)""")
    cursor.execute("""create index deptfk on employee (dept)""")
    cursor.execute("""create index mgr on employee (manager)""")
    cursor.execute("""create index emplid on user (employeeid)""")
    cursor.execute("""create index deptmgr on department (manager)""")

    connection.commit()
    connection.close()


def insert_values_in_db(db_file):
    connection = sqlite3.connect(db_file)
    cursor = connection.cursor()
    cursor.execute(
        """Insert into department (departmentid, name, manager) values (123, 'banker', 999)"""
    )
    connection.commit()
    cursor.close()


def retrive_values_from_db(db_file):
    connection = sqlite3.connect(db_file)
    cursor = connection.cursor()
    cursor.execute("""select * from department where name!= 'banker';""")
    data = cursor.fetchone()
    print("fetchone data:{}".format(data))

    data = cursor.fetchall()
    print("fetchall data:{}".format(data))

    cursor.close()


if __name__ == "__main__":
    create_connection("pythonsqlite.db")
    create_tables("pythonsqlite.db")
    # create_indexes_for_db("pythonsqlite.db")
    insert_values_in_db("pythonsqlite.db")
    retrive_values_from_db("pythonsqlite.db")
