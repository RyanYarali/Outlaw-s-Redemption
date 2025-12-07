import unittest
from game import display_game_over


class TestDisplayGameOver(unittest.TestCase):
    
    def test_runs_without_error(self):
        try:
            display_game_over()
            result = True
        except Exception:
            result = False
        self.assertTrue(result)
    
    def test_can_be_called_multiple_times(self):
        try:
            display_game_over()
            display_game_over()
            result = True
        except Exception:
            result = False
        self. assertTrue(result)
    
    def test_returns_none(self):
        result = display_game_over()
        self.assertIsNone(result)


if __name__ == '__main__':
    unittest.main()
