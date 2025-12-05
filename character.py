"""
Ryan Yarali
A01464263

Manages player character creation, stats, and progression.
"""
from color import *


def make_character(name: str) -> dict:
    """
    Create and return a new player character dictionary.

    :param name: the player's chosen name
    :precondition: name must be a nonempty string
    :postcondition: creates a character dictionary with default starting values
    :return: dictionary representing the player character

    >>> player = make_character("Jesse")
    >>> player["Name"]
    'Jesse'
    >>> player["Current HP"]
    100
    """
    return {
        "Name": name,
        "X-coordinate": 0,
        "Y-coordinate": 0,
        "Current HP": 100,
        "Maximum HP": 100,
        "Honor": 0,
        "Level": 1,
        "XP": 0,
        "Gold": 50,
        "Supplies": 3,
    }


def is_alive(character: dict) -> bool:
    """
    Check if the character is still alive.

    :param character: a dictionary representing the player character
    :precondition: character must have a Current HP key
    :postcondition: determines if character's HP is greater than zero
    :return: True if character is alive, False otherwise

    >>> test_char = {"Current HP": 50}
    >>> is_alive(test_char)
    True
    """
    return character.get("Current HP", 0) > 0


def gain_xp(character: dict, amount: int):
    """
    Add experience points to the character.

    :param character: a dictionary representing the player character
    :param amount: the amount of XP to add
    :precondition: character must have an XP key
    :precondition: amount must be a non-negative integer
    :postcondition: increases the character's XP by the specified amount
    :return: None

    >>> test_char = {"XP": 50}
    >>> gain_xp(test_char, 25)
    >>> test_char["XP"]
    75
    """
    character["XP"] = character.get("XP", 0) + amount


def character_has_leveled(character: dict) -> bool:
    """
    Check if the character has enough XP to level up.

    :param character: a dictionary representing the player character
    :precondition: character must have XP and Level keys
    :postcondition: determines if character meets XP threshold for next level
    :return: True if character can level up, False otherwise

    >>> test_char = {"XP": 120, "Level": 1}
    >>> character_has_leveled(test_char)
    True
    """
    xp_amount = character.get("XP", 0)
    level = character.get("Level", 1)

    if level == 1 and xp_amount >= 100:
        return True
    if level == 2 and xp_amount >= 250:
        return True
    return False


def level_up_character(character: dict):
    """
    Increase the character level and improve stats.

    :param character: a dictionary representing the player character
    :precondition: character must have Level, Maximum HP and Current HP keys
    :postcondition: increases level by 1, increases Maximum HP by 50, and restores HP
    :return: None

    >>> test_char = {"Level": 1, "Maximum HP": 100, "Current HP": 50}
    >>> level_up_character(test_char)
    >>> test_char["Level"]
    2
    >>> test_char["Maximum HP"]
    150
    """
    current_level = character.get("Level", 1)
    character["Level"] = current_level + 1
    character["Maximum HP"] = character.get("Maximum HP", 100) + 50
    character["Current HP"] = character["Maximum HP"]


def display_character_stats(character: dict):
    """
    Print the character current statistics

    :param character: a dictionary representing the player character
    :precondition: character must have all stat keys
    :postcondition: prints formatted character stats to console
    :return: None

    """
    print(MAGENTA + "\n<[ S T A T S ]>" + RESET)
    print()
    print(MAGENTA + f"NAME:   {character['Name']}" + RESET)
    print(MAGENTA + f"LEVEL:  {character['Level']}" + RESET)
    print(MAGENTA + f"XP:     {character['XP']}" + RESET)
    print(MAGENTA + f"HP:     {character['Current HP']}/{character['Maximum HP']}" + RESET)
    print(MAGENTA + f"HONOR:  {character['Honor']}" + RESET)
    print(MAGENTA + f"GOLD:   {character['Gold']}" + RESET)
    print(MAGENTA + "\n[-------------]\n" + RESET)


