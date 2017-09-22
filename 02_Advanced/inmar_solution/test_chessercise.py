import unittest
from chessercise import *
""""
Unit test script for chessercise.py file
"""

class TestConstants(unittest.TestCase):
    def test_constants(self):
        self.assertEqual(ROWS_ALPHABETS, ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])
        self.assertEqual(ROWS, [97, 98, 99, 100, 101, 102, 103, 104])
        self.assertEqual(COLUMNS, [1, 2, 3, 4, 5, 6, 7, 8])

        self.assertEqual(all_fields_display,
                         ['a1', 'b1', 'c1', 'd1', 'e1', 'f1', 'g1', 'h1', 'a2', 'b2', 'c2', 'd2', 'e2', 'f2', 'g2',
                          'h2', 'a3', 'b3', 'c3', 'd3', 'e3', 'f3', 'g3', 'h3', 'a4', 'b4', 'c4', 'd4', 'e4', 'f4',
                          'g4', 'h4', 'a5', 'b5', 'c5', 'd5', 'e5', 'f5', 'g5', 'h5', 'a6', 'b6', 'c6', 'd6', 'e6',
                          'f6', 'g6', 'h6', 'a7', 'b7', 'c7', 'd7', 'e7', 'f7', 'g7', 'h7', 'a8', 'b8', 'c8', 'd8',
                          'e8', 'f8', 'g8', 'h8'])


class TestKnight(unittest.TestCase):
    def __init__(self):
        self.assertEqual(ROWS_ALPHABETS, ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])

class TestRook(unittest.TestCase):
    def __init__(self):
        self.assertEqual(ROWS_ALPHABETS, ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])

class TestQueen(unittest.TestCase):
    def __init__(self):
        self.assertEqual(ROWS_ALPHABETS, ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])

if __name__ == '__main__':
    print all_fields_display
    unittest.main()
