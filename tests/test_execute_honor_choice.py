import unittest
from encounters import execute_honor_choice
from unittest.mock import patch


class TestExecuteHonorChoice(unittest.TestCase):

    @patch('builtins.input', side_effect=['1', '1', '1', '1', '1'])
    def test_function_runs_without_error(self, __):
        character = {"XP": 0, "Gold": 0, "Honor": 0}
        try:
            execute_honor_choice(character)
            result = True
        except Exception:
            result = False
        self.assertTrue(result)

    @patch('builtins.input', side_effect=['2', '2', '2', '2', '2'])
    def test_character_has_xp_key(self, __):
        character = {"XP": 0, "Gold": 0, "Honor": 0}
        execute_honor_choice(character)
        self.assertIn("XP", character)

    @patch('builtins.input', side_effect=['3', '3', '3', '3', '3'])
    def test_character_has_honor_key(self, __):
        character = {"XP": 0, "Gold": 0, "Honor": 0}
        execute_honor_choice(character)
        self.assertIn("Honor", character)


if __name__ == '__main__':
    unittest.main()