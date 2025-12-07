import unittest
from character import make_character


class TestMakeCharacter(unittest.TestCase):
    
    def test_returns_dictionary(self):
        character = make_character("TestHero")
        self.assertIsInstance(character, dict)
    
    def test_has_correct_name(self):
        character = make_character("TestHero")
        self.assertEqual(character["Name"], "TestHero")
    
    def test_starts_at_origin(self):
        character = make_character("TestHero")
        self.assertEqual(character["X-coordinate"], 0)
        self. assertEqual(character["Y-coordinate"], 0)


if __name__ == '__main__':
    unittest.main()
