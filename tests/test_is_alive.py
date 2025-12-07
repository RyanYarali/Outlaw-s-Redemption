import unittest
from character import is_alive


class TestIsAlive(unittest.TestCase):
    
    def test_with_positive_hp(self):
        character = {"Current HP": 50}
        self.assertTrue(is_alive(character))
    
    def test_with_zero_hp(self):
        character = {"Current HP": 0}
        self.assertFalse(is_alive(character))
    
    def test_with_negative_hp(self):
        character = {"Current HP": -10}
        self. assertFalse(is_alive(character))


if __name__ == '__main__':
    unittest.main()
