import unittest


class TestArithmeticOperations(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print("SetupClass")

    def setUp(self) -> None:
        print("\nsetUp")

    def test01(self):
        print("test01")

    def test02(self):
        print("test02")

    def tearDown(self) -> None:
        print("tearDown\n")

    @classmethod
    def tearDownClass(cls) -> None:
        print("\ntearDownClass")
