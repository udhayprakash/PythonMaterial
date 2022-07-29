#!/usr/bin/python
import os
import unittest

import mock


def simple_urandom(length):
    return "f" * length


class TestRandom(unittest.TestCase):
    @mock.patch("os.urandom", side_effect=simple_urandom)
    def test_urandom(self, urandom_function):
        assert os.urandom(5) == "fffff"
