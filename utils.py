"""
Ryan Yarali
A01464263

Provides input validation and character movement.
"""
from color import *

def validate_move(board: dict, character: dict, direction: str) -> bool:
    """
    Check if a move in the given direction is valid.

    :param board: a dictionary representing the game board
    :param character: a dictionary representing the player character
    :param direction: a string representing the direction ('N', 'S', 'E', 'W')
    :precondition: board must be a valid board dictionary with row, column keys
    :precondition: character must have x coordinate and y coordinate keys
    :precondition: direction must be one of N, S, E, W
    :postcondition: determines if the move stays within board boundaries
    :return: True if move is valid, False otherwise

    >>> test_board = {(0, 0): {}, (0, 1): {}}
    >>> test_char = {"X-coordinate": 0, "Y-coordinate": 0}
    >>> validate_move(test_board, test_char, 'N')
    False
    """
    current_x = character["X-coordinate"]
    current_y = character["Y-coordinate"]

    direction_map = {
        "N": (0, -1),
        "S": (0, 1),
        "E": (1, 0),
        "W": (-1, 0),
    }

    if direction not in direction_map:
        return False

    delta_x, delta_y = direction_map[direction]
    new_x = current_x + delta_x
    new_y = current_y + delta_y

    return (new_y, new_x) in board


def move_character(character: dict, direction: str):
    """
    Move the character in the specified direction.

    :param character: a dictionary representing the player character
    :param direction: a string representing the direction N, S, E, W
    :precondition: character must have x coordinate and y coordinate keys
    :precondition: direction must be one of N, S, E, W
    :postcondition: updates character's coordinates based on direction
    :return: None

    >>> test_char = {"X-coordinate": 5, "Y-coordinate": 5}
    >>> move_character(test_char, 'N')
    >>> test_char["Y-coordinate"]
    4
    """
    direction_map = {
        "N": (0, -1),
        "S": (0, 1),
        "E": (1, 0),
        "W": (-1, 0),
    }

    if direction in direction_map:
        delta_x, delta_y = direction_map[direction]
        character["X-coordinate"] += delta_x
        character["Y-coordinate"] += delta_y


def get_user_choice() -> str:
    """
    Prompt the user for a game choice with a stylized prompt.

    :precondition: none
    :postcondition: prompts user for input and returns uppercase string
    :return: user's choice as uppercase string
    """
    prompt = f"\n{CYAN}Your move?  [N/S/E/W = Move, M = Map, I = Info, $ = Shop, Q = Quit]{RESET}\n>>> "
    choice = input(prompt).strip().upper()
    return choice


