import unittest

from api_access import api


class TetsApi(unittest.TestCase):
    def test_api(self):
        assert api() == 200
