import unittest
from board import make_board, get_location_description


class TestGetLocationDescription(unittest.TestCase):
    
    def test_returns_string(self):
        board = make_board(10, 10)
        result = get_location_description(board, 0, 0)
        self.assertIsInstance(result, str)
    
    def test_returns_non_empty_string(self):
        board = make_board(10, 10)
        result = get_location_description(board, 5, 5)
        self. assertGreater(len(result), 0)
    
    def test_different_locations_different_descriptions(self):
        board = make_board(10, 10)
        desc1 = get_location_description(board, 0, 0)
        desc2 = get_location_description(board, 9, 9)
        self. assertNotEqual(desc1, desc2)


if __name__ == '__main__':
    unittest.main()
