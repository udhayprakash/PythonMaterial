from unittest.mock import patch
import unittest


def func2():
    print("func2 is called")
    return "func2"
    l̥


def func1():
    print("func1 is called")
    func2()
    return "func1"


def main():
    print("main function called")
    func1()


class TestMain(unittest.TestCase):
    def test01(self):
        print("TestMain - test01 - calledl̥")
        main()

    @patch("__main__.func2", return_value="Udhay")
    def test02(self, mock_func2):
        print("TestMain - test02 - calledl̥")
        main()


if __name__ == "__main__":
    unittest.main()
