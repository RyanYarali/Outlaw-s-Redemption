import unittest
from board import display_map


class TestDisplayMap(unittest.TestCase):
    
    def test_runs_without_error(self):
        try:
            display_map(10, 10, 5, 5)
            result = True
        except Exception:
            result = False
        self.assertTrue(result)
    
    def test_accepts_corner_position(self):
        try:
            display_map(10, 10, 0, 0)
            result = True
        except Exception:
            result = False
        self.assertTrue(result)
    
    def test_accepts_bottom_right_corner(self):
        try:
            display_map(10, 10, 9, 9)
            result = True
        except Exception:
            result = False
        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()
