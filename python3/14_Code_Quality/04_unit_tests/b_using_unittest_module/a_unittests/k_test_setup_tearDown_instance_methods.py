"""
Purpose: unit testing

    test case life cycle
        - born  - setup method
        - before death - tearDown method
"""


import unittest


class TestCaseDemo(unittest.TestCase):
    def setUp(self):
        print("\nsetUp method execution ...")

    def tearDown(self) -> None:
        print("tearDown method execution ...")

    def test01_something(self):
        print("In test01_something")

    def test02_someotherthing(self):
        print("In test02_someotherthing")

    def test03_someotherthing(self):
        print("In test03_someotherthing")


if __name__ == "__main__":
    unittest.main()

"""
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
"""
