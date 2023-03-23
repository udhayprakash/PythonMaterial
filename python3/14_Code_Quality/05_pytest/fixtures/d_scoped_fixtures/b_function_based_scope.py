import pytest


@pytest.fixture(scope="function")
def function_scope_fixture():
    "Run once per test function"
    return "Today is Good Day"


def test_function_1(function_scope_fixture):
    assert function_scope_fixture == "Today is Good Day"


def test_function_2(function_scope_fixture):
    assert function_scope_fixture != "Tomorrow is Good Day"
