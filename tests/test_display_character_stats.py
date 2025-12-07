import unittest
from character import display_character_stats


class TestDisplayCharacterStats(unittest.TestCase):
    
    def test_runs_without_error(self):
        character = {"Name": "Test", "Level": 1, "XP": 50, "Current HP": 100, "Maximum HP": 100, "Gold": 100, "Honor": 0}
        try:
            display_character_stats(character)
            result = True
        except Exception:
            result = False
        self.assertTrue(result)
    
    def test_accepts_high_level_character(self):
        character = {"Name": "Test", "Level": 3, "XP": 500, "Current HP": 200, "Maximum HP": 200, "Gold": 1000, "Honor": 100}
        try:
            display_character_stats(character)
            result = True
        except Exception:
            result = False
        self.assertTrue(result)
    
    def test_accepts_negative_honor(self):
        character = {"Name": "Test", "Level": 2, "XP": 150, "Current HP": 150, "Maximum HP": 150, "Gold": 500, "Honor": -50}
        try:
            display_character_stats(character)
            result = True
        except Exception:
            result = False
        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()
