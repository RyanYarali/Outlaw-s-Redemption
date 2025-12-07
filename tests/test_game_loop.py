import unittest
from game import game_loop
from unittest.mock import patch


class TestGameLoop(unittest.TestCase):
    
    @patch('builtins.input', side_effect=['TestHero', 'Q'])
    def test_accepts_quit_command(self, __):
        try:
            game_loop(10, 10, 0)
            result = True
        except Exception:
            result = False
        self.assertTrue(result)
    
    @patch('builtins.input', side_effect=['TestHero', 'Q'])
    def test_runs_with_small_board(self, __):
        try:
            game_loop(3, 3, 0)
            result = True
        except Exception:
            result = False
        self.assertTrue(result)
    
    @patch('builtins.input', side_effect=['TestHero', 'Q'])
    def test_runs_with_zero_encounter_chance(self, __):
        try:
            game_loop(10, 10, 0)
            result = True
        except Exception:
            result = False
        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()
