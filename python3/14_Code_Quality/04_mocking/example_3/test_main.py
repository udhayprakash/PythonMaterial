import unittest

from main import api


class TetsApi(unittest.TestCase):
    def test_api(self):
        assert api() == 200
