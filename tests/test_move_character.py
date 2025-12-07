import unittest
from utils import move_character


class TestMoveCharacter(unittest.TestCase):
    
    def test_move_north_decreases_y(self):
        character = {"X-coordinate": 5, "Y-coordinate": 5}
        move_character(character, 'N')
        self.assertEqual(character["Y-coordinate"], 4)
    
    def test_move_south_increases_y(self):
        character = {"X-coordinate": 5, "Y-coordinate": 5}
        move_character(character, 'S')
        self.assertEqual(character["Y-coordinate"], 6)
    
    def test_move_east_increases_x(self):
        character = {"X-coordinate": 5, "Y-coordinate": 5}
        move_character(character, 'E')
        self.assertEqual(character["X-coordinate"], 6)


if __name__ == '__main__':
    unittest.main()
