import sqlite3


def get_cursor():
    conn = sqlite3.connect("books.db")
    return conn.cursor()


def select_all_records_by_author(cursor, author):
    sql = "SELECT * FROM books WHERE author=?"
    cursor.execute(sql, [author])
    print(cursor.fetchall())  # or use fetchone()
    print("\nHere is a listing of the rows in the table\n")
    for row in cursor.execute("SELECT rowid, * FROM books ORDER BY author"):
        print(row)


def select_using_like(cursor, text):
    print("\nLIKE query results:\n")
    sql = """
    SELECT * FROM books
    WHERE title LIKE ?"""
    cursor.execute(sql, ('{0}%'.format(text), ))
    print(cursor.fetchall())


if __name__ == "__main__":
    cursor = get_cursor()
    select_all_records_by_author(cursor, author="Mike Driscoll")
    select_using_like(cursor, text="Python")
