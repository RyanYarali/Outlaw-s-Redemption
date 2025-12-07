import unittest
from board import make_board


class TestMakeBoard(unittest. TestCase):
    
    def test_creates_correct_size(self):
        board = make_board(10, 10)
        self. assertEqual(len(board), 100)
    
    def test_small_board_size(self):
        board = make_board(3, 3)
        self. assertEqual(len(board), 9)
    
    def test_has_valid_coordinate_keys(self):
        board = make_board(5, 5)
        self.assertIn((0, 0), board)
        self.assertIn((4, 4), board)
        self.assertIn((2, 3), board)


if __name__ == '__main__':
    unittest.main()
