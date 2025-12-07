import unittest
from combat import execute_combat_encounter
from unittest.mock import patch


class TestExecuteCombatEncounter(unittest.TestCase):

    @patch('builtins.input', return_value='1')
    def test_high_hp_character_survives(self, __):
        character = {"Current HP": 1000, "Level": 3, "XP": 0, "Gold": 0}
        result = execute_combat_encounter(character)
        self. assertTrue(result)

    @patch('builtins.input', return_value='1')
    def test_modifies_character_stats(self, __):
        character = {"Current HP": 1000, "Level": 1, "XP": 0, "Gold": 50}
        execute_combat_encounter(character)
        self.assertIsInstance(character["Current HP"], int)

    @patch('builtins.input', return_value='1')
    def test_adds_gold_on_victory(self, __):
        character = {"Current HP": 1000, "Level": 3, "XP": 0, "Gold": 0}
        initial_gold = character["Gold"]
        execute_combat_encounter(character)
        self. assertGreater(character["Gold"], initial_gold)


if __name__ == '__main__':
    unittest.main()