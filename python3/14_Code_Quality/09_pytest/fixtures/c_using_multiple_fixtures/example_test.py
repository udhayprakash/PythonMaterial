import pytest

@pytest.fixture
def allowed_input_list():
    return [1,2,3,4,5]

@pytest.fixture
def allowed_output_list():
    return [10,20,30]

def test_my_fixture(allowed_input_list, allowed_output_list):
    input_number = 4
    assert input_number in allowed_input_list
    assert input_number * 5 in allowed_output_list