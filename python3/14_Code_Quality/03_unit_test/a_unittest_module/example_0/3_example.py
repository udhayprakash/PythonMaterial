import time
import unittest

import timeout_decorator


class TimeOutTest(unittest.TestCase):

    @timeout_decorator.timeout(5)
    def test_timeout(self):
        print('start')

    for i in range(1, 10):
        time.sleep(1)
        print(f'{i} seconds have passed')


if __name__ == '__main__':
    unittest.main()
