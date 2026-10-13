"""
Ryan Yarali

Starts the Outlaw's Redemption game.
"""
from game import game_loop


def main():
    """
    Drive the program.
    """
    board_size_rows = 10
    board_size_columns = 10
    encounter_chance_percent = 60

    game_loop(board_size_rows, board_size_columns, encounter_chance_percent)


if __name__ == "__main__":
    main()