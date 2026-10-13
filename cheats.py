"""
Ryan Yarali

Cheat code system.
"""

from color import *


def check_cheat_code(code: str, character: dict) -> bool:
    """
    Check if the input is a valid cheat code and apply its effect.

    :param code: the input string to check
    :param character: the player character dictionary
    :precondition: code must be a string
    :precondition: character must have valid stat keys
    :postcondition: applies cheat effects if code is valid
    :return: True if valid cheat code, False otherwise
    """
    code = code.upper().strip()

    if code == "HEAL":
        character["Current HP"] = character["Maximum HP"]
        print(GREEN + "Full health restored!" + RESET)
        return True

    elif code == "GOLD":
        character["Gold"] += 500
        print(YELLOW + "+500 GOLD!" + RESET)
        return True

    elif code == "LEVEL_UP":
        character["Level"] = 3
        character["XP"] = 250
        character["Maximum HP"] = 200
        character["Current HP"] = 200
        print(MAGENTA + "You're now Level 3!" + RESET)
        return True

    elif code == "BOSS":
        character["X-coordinate"] = 9
        character["Y-coordinate"] = 9
        print(CYAN + "Teleported to boss location (9, 9)!" + RESET)
        return True

    elif code == "GOD":
        character["Current HP"] = 999
        character["Maximum HP"] = 999
        character["Gold"] = 9999
        character["Level"] = 3
        print(RED + "🔥 GOD MODE!  All stats maxed!" + RESET)
        return True

    return False