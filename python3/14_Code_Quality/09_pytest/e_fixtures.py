# Standard imports
import requests
import sqlite3

# Third party imports
import pytest


@pytest.fixture
def setup_database():
    """ Fixture to set up the in-memory database with test data """
    conn = sqlite3.connect(':memory:')
    cursor = conn.cursor()
    cursor.execute('''
	    CREATE TABLE stocks
        (date text, trans text, symbol text, qty real, price real)''')
    sample_data = [
        ('2020-01-01', 'BUY', 'IBM', 1000, 45.0),
        ('2020-01-01', 'SELL', 'GOOG', 40, 123.0),
    ]
    cursor.executemany('INSERT INTO stocks VALUES(?, ?, ?, ?, ?)', sample_data)
    yield conn


def test_connection(setup_database):
    # Test to make sure that there are 2 items in the database

    cursor = setup_database
    assert len(list(cursor.execute('SELECT * FROM stocks'))) == 2
