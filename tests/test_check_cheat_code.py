import unittest
from cheats import check_cheat_code


class TestCheckCheatCode(unittest.TestCase):
    
    def test_heal_cheat_restores_hp(self):
        character = {"Current HP": 50, "Maximum HP": 100}
        result = check_cheat_code("HEAL", character)
        self. assertTrue(result)
        self.assertEqual(character["Current HP"], 100)
    
    def test_gold_cheat_adds_gold(self):
        character = {"Gold": 0}
        result = check_cheat_code("GOLD", character)
        self.assertTrue(result)
        self.assertEqual(character["Gold"], 500)
    
    def test_invalid_code_returns_false(self):
        character = {"Current HP": 50}
        result = check_cheat_code("INVALIDCODE", character)
        self. assertFalse(result)


if __name__ == '__main__':
    unittest.main()
