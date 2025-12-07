import unittest
from game import display_victory_ending


class TestDisplayVictoryEnding(unittest.TestCase):
    
    def test_runs_without_error_high_honor(self):
        character = {"Honor": 100, "Gold": 500}
        try:
            display_victory_ending(character)
            result = True
        except Exception:
            result = False
        self.assertTrue(result)
    
    def test_runs_without_error_low_honor(self):
        character = {"Honor": 0, "Gold": 500}
        try:
            display_victory_ending(character)
            result = True
        except Exception:
            result = False
        self.assertTrue(result)
    
    def test_accepts_negative_honor(self):
        character = {"Honor": -50, "Gold": 1000}
        try:
            display_victory_ending(character)
            result = True
        except Exception:
            result = False
        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()
