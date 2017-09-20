import unittest


class TestknightMoves(unittest.TestCase):
    def test_center(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_corners(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_sides(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)


            # print 'KNIGHT MOVES'
            # print 'center             :(100, 5)     :', knightMoves(100, 5)
            # print 'left top-corner    :(97, 1)      :', knightMoves(97, 1)
            # print 'right top-corner   :(104, 1)     :', knightMoves(104, 1)
            # print 'left bottom-corner :(97, 8)      :', knightMoves(97, 8)
            # print 'right bottom-corner:(104, 8)     :', knightMoves(104, 8)
            # print
            # print 'top middle         :(100, 1)     :', knightMoves(100, 1)
            # print 'left middle        :(97, 4)      :', knightMoves(97, 4)
            # print 'right middle       :(104, 4)     :', knightMoves(104, 4)
            # print 'bottom middle      :(100, 8)     :', knightMoves(100, 8)
            #


if __name__ == '__main__':
    unittest.main()
