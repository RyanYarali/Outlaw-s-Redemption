import unittest
from utils import get_user_choice
from unittest.mock import patch


class TestGetUserChoice(unittest.TestCase):
    
    @patch('builtins.input', return_value='N')
    def test_returns_uppercase_n(self, __):
        result = get_user_choice()
        self.assertEqual(result, 'N')
    
    @patch('builtins.input', return_value='s')
    def test_converts_lowercase_to_uppercase(self, __):
        result = get_user_choice()
        self.assertEqual(result, 'S')
    
    @patch('builtins.input', return_value='  m  ')
    def test_strips_whitespace(self, __):
        result = get_user_choice()
        self. assertEqual(result, 'M')


if __name__ == '__main__':
    unittest.main()
