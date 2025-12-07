import unittest
from encounters import check_for_challenges


class TestCheckForChallenges(unittest.TestCase):
    
    def test_with_100_percent_chance(self):
        result = check_for_challenges(100)
        self.assertTrue(result)
    
    def test_with_0_percent_chance(self):
        result = check_for_challenges(0)
        self.assertFalse(result)
    
    def test_returns_boolean(self):
        result = check_for_challenges(50)
        self.assertIsInstance(result, bool)


if __name__ == '__main__':
    unittest.main()
