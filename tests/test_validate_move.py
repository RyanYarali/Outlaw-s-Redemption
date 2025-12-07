import unittest
from utils import validate_move
from board import make_board


class TestValidateMove(unittest.TestCase):
    
    def test_north_from_middle_is_valid(self):
        board = make_board(10, 10)
        character = {"X-coordinate": 5, "Y-coordinate": 5}
        self.assertTrue(validate_move(board, character, 'N'))
    
    def test_north_from_edge_is_invalid(self):
        board = make_board(10, 10)
        character = {"X-coordinate": 5, "Y-coordinate": 0}
        self.assertFalse(validate_move(board, character, 'N'))
    
    def test_south_from_middle_is_valid(self):
        board = make_board(10, 10)
        character = {"X-coordinate": 5, "Y-coordinate": 5}
        self.assertTrue(validate_move(board, character, 'S'))


if __name__ == '__main__':
    unittest.main()
