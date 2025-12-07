import unittest
from encounters import execute_challenge_protocol
from unittest.mock import patch


class TestExecuteChallengeProtocol(unittest.TestCase):

    @patch('builtins.input', return_value='1')
    def test_returns_boolean(self, __):
        character = {"Current HP": 1000, "Level": 3, "XP": 0, "Gold": 0, "Honor": 0}
        result = execute_challenge_protocol(character, "combat")
        self.assertIsInstance(result, bool)

    @patch('builtins.input', return_value='1')
    def test_high_hp_survives_combat(self, __):
        character = {"Current HP": 1000, "Level": 3, "XP": 0, "Gold": 0, "Honor": 0}
        result = execute_challenge_protocol(character, "combat")
        self.assertTrue(result)

    @patch('builtins.input', side_effect=['1', '1', '1', '1', '1'])
    def test_accepts_choice_encounter(self, __):
        character = {"Current HP": 100, "Level": 1, "XP": 0, "Gold": 0, "Honor": 0}
        try:
            execute_challenge_protocol(character, "choice")
            result = True
        except Exception:
            result = False
        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()