"""
Purpose: unit testing

setupClass & tearDownClass methods are executed ONCE, per test suite
setUp & tearDown methods are executed for each test case


setupClass

    setUp
    test_case_1
    tearDown

    setUp
    test_case_2
    tearDown

    ...

tearDownClass
"""

import unittest


class TestCaseDemo(unittest.TestCase):  # TestSuite
    @classmethod
    def setUpClass(cls) -> None:
        print("setUpClass method executed ...")

    @classmethod
    def tearDownClass(cls) -> None:
        print("tearDownClass method executed ...")

    def setUp(self):
        print("\n\tsetUp method execution ...")

    def tearDown(self) -> None:
        print("\ttearDown method execution ...")

    def test01_something(self):
        print("\t\tIn test01_something")

    def test02_someotherthing(self):
        print("\t\tIn test02_someotherthing")

    def test03_someotherthing(self):
        print("\t\tIn test03_someotherthing")


if __name__ == "__main__":
    unittest.main()

"""
setUpClass method executed ...

        setUp method execution ...
                In test01_something
        tearDown method execution ...
.
        setUp method execution ...
                In test02_someotherthing
        tearDown method execution ...
.
        setUp method execution ...
                In test03_someotherthing
        tearDown method execution ...
.tearDownClass method executed ...


"""
