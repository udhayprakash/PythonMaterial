import sqlite3


def delete_author(author):
    conn = sqlite3.connect("books.db")
    cursor = conn.cursor()

    sql = """
    DELETE FROM books
    WHERE author = ?
    """
    cursor.execute(sql, (author, ))
    conn.commit()


if __name__ == "__main__":
    delete_author(author="Al Sweigart")
