"""

database 
    - relational/structured db 
        - File based 
            - sqlite3
        - port based 
            - mysql 
            - ms sql 
            - oracle 
    - no sql db 
        - port based 
            - mongo db 
            - cassandra db 

"""

import sqlite3
from sqlite3 import Error


def create_connection():
    """ create a database connection to a database that resides
        in the memory
    """
    try:
        conn = sqlite3.connect(':memory:')
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        conn.close()


if __name__ == '__main__':
    create_connection()
