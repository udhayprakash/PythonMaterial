import pytest

@pytest.fixture()
def setup_test_data():
    test_value = 100
    return test_value

def test_function(setup_test_data):
    a = 100
    assert a == setup_test_data