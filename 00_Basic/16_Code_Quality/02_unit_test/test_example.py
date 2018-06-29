#example of unittest module

import unittest
from example import first, last

list_nums = [7,9,5]
list_chars = ['m', 'd', 'Z', 'l']
 
class TestPPMath(unittest.TestCase):
    
    def test_first(self):
        self.assertEqual(first(list_nums), 5)

    def test_last(self):
        self.assertTrue(last(list_chars), 'm')
        
    def testFirstAgain(self):
        self.failUnless(first(list_chars), 'Z')
        
    def testLastAgain(self):
        self.failIf(last(list_nums), 9)



if __name__ == '__main__':
    unittest.main()
        

