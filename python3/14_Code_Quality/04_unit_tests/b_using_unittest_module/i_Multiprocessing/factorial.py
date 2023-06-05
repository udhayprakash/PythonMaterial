import multiprocessing
import unittest


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


# print(factorial(9))


def factorial_process(n, result_queue):
    result_queue.put(factorial(n))


class TestFactorial(unittest.TestCase):
    def test_factorial(self):
        result_queue = multiprocessing.Queue()
        p = multiprocessing.Process(target=factorial_process, args=(5, result_queue))
        p.start()
        p.join()
        result = result_queue.get()
        self.assertEqual(result, 120)
