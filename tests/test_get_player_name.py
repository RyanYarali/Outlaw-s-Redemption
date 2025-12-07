import unittest
from game import get_player_name
from unittest.mock import patch


class TestGetPlayerName(unittest.TestCase):

    @patch('builtins.input', return_value='TestHero')
    def test_returns_string(self, __):
        result = get_player_name()
        self.assertIsInstance(result, str)

    @patch('builtins.input', return_value='TestHero')
    def test_returns_non_empty_name(self, __):
        result = get_player_name()
        self.assertGreater(len(result), 0)

    @patch('builtins.input', return_value='  TestHero  ')
    def test_strips_whitespace(self, __):
        result = get_player_name()
        self.assertEqual(result, 'TestHero')


if __name__ == '__main__':
    unittest.main()