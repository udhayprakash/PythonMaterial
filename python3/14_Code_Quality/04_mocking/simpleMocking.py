import os
import unittest

import mock
import urllib2


def responseStatus(url):
    return urllib2.urlopen(url).msg


class TestRandom(unittest.TestCase):
    @mock.patch("https://api.ipify.org?format=json", side_effect=responseStatus)
    def test_responseStatus(self, urandom_function):
        assert responseStatus("https://api.ipify.org?format=json") == "OK"
