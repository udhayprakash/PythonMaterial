#!/usr/bin/python
"""
Purpose: Performance (time) testing
"""

import time
from unittest import TestCase, main

import timeout_decorator


class TimeOutTest(TestCase):
    @timeout_decorator.timeout(5)
    def test_timeout(self):
        print("start")

        for i in range(1, 10):
            time.sleep(1)
            print(f"{i} seconds have passed")


if __name__ == "__main__":
    main()
