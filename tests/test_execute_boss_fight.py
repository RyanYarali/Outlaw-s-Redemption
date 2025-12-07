import unittest
from game import execute_boss_fight
from unittest.mock import patch


class TestExecuteBossFight(unittest.TestCase):

    @patch('builtins.input', return_value='n')
    def test_returns_boolean(self, __):
        character = {"Current HP": 1000, "Level": 3, "Gold": 0, "Maximum HP": 1000, "XP": 250}
        result = execute_boss_fight(character)
        self.assertIsInstance(result, bool)

    @patch('builtins.input', return_value='n')
    def test_high_hp_character_wins(self, __):
        character = {"Current HP": 1000, "Level": 3, "Gold": 0, "Maximum HP": 1000, "XP": 250}
        result = execute_boss_fight(character)
        self.assertTrue(result)

    @patch('builtins.input', return_value='n')
    def test_low_hp_character_loses(self, __):
        character = {"Current HP": 1, "Level": 3, "Gold": 0, "Maximum HP": 200, "XP": 250}
        result = execute_boss_fight(character)
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()