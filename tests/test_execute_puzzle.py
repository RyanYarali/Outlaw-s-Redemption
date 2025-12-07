import unittest
from encounters import execute_puzzle
from unittest.mock import patch


class TestExecutePuzzle(unittest.TestCase):

    @patch('builtins.input', return_value='testanswer')
    def test_function_runs_without_error(self, __):
        character = {"XP": 0, "Gold": 0}
        try:
            execute_puzzle(character)
            result = True
        except Exception:
            result = False
        self.assertTrue(result)

    @patch('builtins.input', return_value='testanswer')
    def test_character_has_xp_key_after(self, __):
        character = {"XP": 0, "Gold": 0}
        execute_puzzle(character)
        self.assertIn("XP", character)

    @patch('builtins.input', return_value='testanswer')
    def test_character_has_gold_key_after(self, __):
        character = {"XP": 0, "Gold": 0}
        execute_puzzle(character)
        self.assertIn("Gold", character)


if __name__ == '__main__':
    unittest.main()