"""
Fixtures have optional arguments called scope. The scope parameters has the following values.

    1) function (default scope)
    2) session
    3) class
    4) module
    5) package

"""
import pytest


@pytest.fixture(scope="class")
def class_scope_fixture():
    "Run once per test class"
    pass


@pytest.fixture(scope="session")
def session_scope_fixture():
    "Run once per test session"
    pass


@pytest.fixture(scope="module")
def module_scope_fixture():
    "Run once per test module"
    pass


@pytest.mark.usefixtures(class_scope_fixture)
class TestFixture:
    def test_1(self):
        pass

    def test_2(self):
        pass
