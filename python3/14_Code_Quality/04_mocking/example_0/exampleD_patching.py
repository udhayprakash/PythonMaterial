import os
import unittest
from unittest import mock

print(os.listdir())  # ['a_mocking.ipynb', 'b_mocking.py', 'c_mock_patch.py']


class TestOSDir(unittest.TestCase):
    @mock.patch("os.listdir", mock.MagicMock(return_value="test1"))
    def test1(self):
        assert "test1" == os.listdir()
        self.assertEqual("test1", os.listdir())

    @mock.patch("os.listdir")
    def test2(self, mock_listdir):
        mock_listdir.return_value = "test2"

        assert "test2" == os.listdir()
        self.assertEqual("test2", os.listdir())


@mock.patch("os.listdir")
class TestSuite:
    def test_not_decorated_and_not_tested(self):
        assert False

    def test3(self, mock_listdir):
        mock_listdir.return_value = "test3"
        assert "test3" == os.listdir()
        self.assertEqual("test3", os.listdir())


if __name__ == "__main__":
    unittest.main()
