import pytest


@pytest.fixture
def input_value():
    return 10


def test_addition(input_value):
    assert input_value + 10 == 20


def test_addition_two(input_value):
    assert input_value + -10 == 0


@pytest.mark.skip
def test_addition_three(input_value):
    assert 20 + -10 == 0
