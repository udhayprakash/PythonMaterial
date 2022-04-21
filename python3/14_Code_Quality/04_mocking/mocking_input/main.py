import unittest
from unittest.mock import patch


def yes_or_no():
    answer = input('Do you want to quit? > ')
    if answer == 'yes':
        return('Quitter!')
    elif answer == 'no':
        return('Awesome!')
    else:
        return('BANG!')


class TestQuitting(unittest.TestCase):
    def test_quitting(self):
        with patch('builtins.input', return_value='yes'):
            self.assertEqual(yes_or_no(), 'Quitter!')

        with patch('builtins.input', return_value='no'):
            self.assertEqual(yes_or_no(), 'Awesome!')

if __name__ == '__main__':
    unittest.main(verbosity=2)
