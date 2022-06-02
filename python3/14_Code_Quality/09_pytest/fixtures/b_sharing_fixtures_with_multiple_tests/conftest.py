import pytest 

@pytest.fixture
def get_db_driver():
    return "psycopg"
