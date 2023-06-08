import os
import unittest
from unittest import mock

print(os.listdir())
# ['exampleA.py', 'exampleB.py', 'exampleC.py', 'exampleD_patching.py']


class TestOSDir(unittest.TestCase):
    @mock.patch("os.listdir", mock.MagicMock(return_value="test1"))
    def test1(self):
        # assert "test1" == os.listdir()
        self.assertEqual("test1", os.listdir())

    @mock.patch("os.listdir", mock.MagicMock(return_value=["test1"]))
    def test2(self):
        # assert ["test1"] == os.listdir()
        self.assertEqual(["test1"], os.listdir())

    @mock.patch("os.listdir")
    def test3(self, mock_listdir):
        mock_listdir.return_value = ("test1", "test2")

        assert "test1" in os.listdir()
        assert "test2" in os.listdir()
        assert ("test1", "test2") == os.listdir()

        self.assertEqual(("test1", "test2"), os.listdir())


@mock.patch("os.listdir")
class TestSuite(unittest.TestCase):
    @unittest.skip("skipping")
    def test_not_decorated_and_not_tested(self):
        assert False

    def test3(self, mock_listdir):
        mock_listdir.return_value = "test3"
        assert "test3" == os.listdir()
        self.assertEqual("test3", os.listdir())
