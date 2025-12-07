import unittest
from character import level_up_character


class TestLevelUpCharacter(unittest.TestCase):
    
    def test_increases_level(self):
        character = {"Level": 1, "Maximum HP": 100, "Current HP": 50}
        level_up_character(character)
        self.assertEqual(character["Level"], 2)
    
    def test_increases_maximum_hp(self):
        character = {"Level": 1, "Maximum HP": 100, "Current HP": 50}
        level_up_character(character)
        self.assertEqual(character["Maximum HP"], 150)
    
    def test_restores_current_hp(self):
        character = {"Level": 1, "Maximum HP": 100, "Current HP": 50}
        level_up_character(character)
        self.assertEqual(character["Current HP"], 150)


if __name__ == '__main__':
    unittest.main()
