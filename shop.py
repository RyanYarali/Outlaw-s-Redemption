"""
Ryan Yarali

Allows players to spend gold on supplies.
"""

from color import *


def display_shop():
    print(CYAN + r"""

    ╔════════════════════════════════════════════╗
    ║         DUSTY GULCH GENERAL STORE          ║
    ║           "Fair Prices, Maybe"             ║
    ╚════════════════════════════════════════════╝

         _______________
        |   [][][]      |
        |   [][][]      |     The old shopkeeper nods. 
        |   [][][]      |     "What can I get ya?"
        |_______________|

    """ + RESET)


def shop_menu(character: dict):
    """
    Display shop and allow player to buy items.

    :param character: player character dictionary
    :precondition: character must have Gold, Current HP and XP keys
    :postcondition: player can purchase items with gold
    :return: None

    >>> test_char = {"Gold": 100, "Current HP": 50, "Maximum HP": 100, "XP": 0}
    >>> shop_menu(test_char)
    """
    while True:
        display_shop()
        print(f"{YELLOW}Your Gold: {character['Gold']}{RESET}")
        print(f"{GREEN}Your HP: {character['Current HP']}/{character['Maximum HP']}{RESET}")
        print(f"{MAGENTA}Your XP: {character.get('XP', 0)}{RESET}\n")

        print("=" * 50)
        print(f"{GREEN}1. Small Health Potion{RESET} (Restore 50 HP) - 30 Gold")
        print(f"{GREEN}2. Large Health Potion{RESET} (Restore 100 HP) - 50 Gold")
        print(f"{BRIGHT_GREEN}3. Full Restoration{RESET} (Restore ALL HP) - 80 Gold")
        print(f"{MAGENTA}4. Experience Boost{RESET} (+25 XP) - 50 Gold")
        print(f"{YELLOW}5. Lucky Charm{RESET} (+50 XP) - 100 Gold")
        print(f"{RED}6. Leave Shop{RESET}")
        print("=" * 50)

        choice = input(CYAN + "\nWhat would you like to buy? >>> " + RESET)

        if choice == "1":
            if character["Gold"] >= 30:
                heal_amount = min(50, character["Maximum HP"] - character["Current HP"])
                if heal_amount > 0:
                    character["Gold"] -= 30
                    character["Current HP"] += heal_amount
                    print(GREEN + f" You drink the small potion. (+{heal_amount} HP)" + RESET)
                else:
                    print(YELLOW + "You're already at full health!" + RESET)
            else:
                print(RED + "  Not enough gold!  (Need 30 gold)" + RESET)

        elif choice == "2":
            if character["Gold"] >= 50:
                heal_amount = min(100, character["Maximum HP"] - character["Current HP"])
                if heal_amount > 0:
                    character["Gold"] -= 50
                    character["Current HP"] += heal_amount
                    print(GREEN + f" You drink the large potion. (+{heal_amount} HP)" + RESET)
                else:
                    print(YELLOW + "You're already at full health!" + RESET)
            else:
                print(RED + "  Not enough gold! (Need 50 gold)" + RESET)

        elif choice == "3":
            if character["Gold"] >= 80:
                heal_amount = character["Maximum HP"] - character["Current HP"]
                if heal_amount > 0:
                    character["Gold"] -= 80
                    character["Current HP"] = character["Maximum HP"]
                    print(BRIGHT_GREEN + f" Fully restored! (+{heal_amount} HP)" + RESET)
                else:
                    print(YELLOW + "You're already at full health!" + RESET)
            else:
                print(RED + "  Not enough gold!  (Need 80 gold)" + RESET)

        elif choice == "4":
            if character["Gold"] >= 50:
                character["Gold"] -= 50
                character["XP"] = character.get("XP", 0) + 25
                print(MAGENTA + " You feel more experienced!  (+25 XP)" + RESET)
            else:
                print(RED + "  Not enough gold! (Need 50 gold)" + RESET)

        elif choice == "5":
            if character["Gold"] >= 100:
                character["Gold"] -= 100
                character["XP"] = character.get("XP", 0) + 50
                print(BRIGHT_MAGENTA + " The charm fills you with knowledge! (+50 XP)" + RESET)
            else:
                print(RED + "  Not enough gold! (Need 100 gold)" + RESET)

        elif choice == "6":
            print(YELLOW + "The shopkeeper waves.  'Come back anytime! '" + RESET)
            break
        else:
            print(RED + "Invalid choice. Try again." + RESET)

        input(CYAN + "\nPress Enter to continue..." + RESET)

