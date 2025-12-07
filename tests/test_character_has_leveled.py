import unittest
from character import character_has_leveled


class TestCharacterHasLeveled(unittest.TestCase):
    
    def test_level_1_to_2_threshold(self):
        character = {"XP": 100, "Level": 1}
        self. assertTrue(character_has_leveled(character))
    
    def test_level_2_to_3_threshold(self):
        character = {"XP": 250, "Level": 2}
        self. assertTrue(character_has_leveled(character))
    
    def test_below_threshold(self):
        character = {"XP": 50, "Level": 1}
        self.assertFalse(character_has_leveled(character))


if __name__ == '__main__':
    unittest.main()
