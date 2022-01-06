import pytest


@pytest.fixture()
def fixture01(request):
    print("\nIn fixture...")
    print("Fixture Scope: " + str(request.scope))
    print("Function Name: " + str(request.function. name))
    print("Class Name: " + str(request.cls))
    print("Module Name: " + str(request.module. name))
    print("File Path: " + str(request.fspath))


# ----- Method 1
def test_case01(fixture01):
    print("\nIn test_case01()...")

# ----- Method 2


@pytest.mark.usefixtures('fixture01')
def test_case01():
    print("\nI'm the test_case01")

# ----- Method 3


@pytest.mark.usefixtures('fixture01')
class TestClass03:
    def test_case01(self):
        print("I'm the test_case01")

    def test_case02(self):
        print("I'm the test_case02")
