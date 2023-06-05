"""
Purpose: Class Based Scope

    class_scope_fixture:
        - This fixture will run once per test class.
        - It can be used for setup that needs to be done once for all the tests in a class.
        - For example, you might use this to set up a database connection that will be reused across multiple tests.
"""
import pytest


@pytest.fixture(scope="class")
def db_connection():
    conn = create_db_connection()
    yield conn
    conn.close()


class TestDatabase:
    def test_insert_data(self, db_connection):
        # Insert some data into the database and verify it was inserted correctly
        pass

    def test_query_data(self, db_connection):
        # Query the data from the database and verify it was retrieved correctly
        pass
