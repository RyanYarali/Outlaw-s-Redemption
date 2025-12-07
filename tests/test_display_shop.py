import unittest
from shop import display_shop


class TestDisplayShop(unittest. TestCase):
    
    def test_runs_without_error(self):
        try:
            display_shop()
            result = True
        except Exception:
            result = False
        self.assertTrue(result)
    
    def test_can_be_called_multiple_times(self):
        try:
            display_shop()
            display_shop()
            display_shop()
            result = True
        except Exception:
            result = False
        self.assertTrue(result)
    
    def test_returns_none(self):
        result = display_shop()
        self.assertIsNone(result)


if __name__ == '__main__':
    unittest.main()
