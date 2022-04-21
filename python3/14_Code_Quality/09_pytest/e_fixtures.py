# Third party imports
import pytest


@pytest.fixture()
def my_fruit():
    return "apple"


def test_fruit(my_fruit):
    assert my_fruit == "apple"


# ======================================================


def setup_database():
    print("setup_database")


def teardown_database():
    print("teardown_database")


@pytest.fixture()
def database_environment():
    setup_database()
    yield
    teardown_database()


def test_world(database_environment):
    assert 1 == 1
