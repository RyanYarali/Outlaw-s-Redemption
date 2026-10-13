"""
Ryan Yarali

Contains the main game loop and game flow logic.
"""
from board import make_board, get_location_description, display_map
from character import make_character, is_alive, character_has_leveled, level_up_character, display_character_stats
from utils import validate_move, move_character, get_user_choice
from encounters import check_for_challenges, determine_encounter_type, execute_challenge_protocol
from shop import shop_menu
from color import *
import random
from cheats import check_cheat_code


def execute_boss_fight(character: dict) -> bool:
    """
    Execute the final boss fight with Sheriff Blackwood.

    :param character: a dictionary representing the player character
    :precondition: character must have Current HP and Level keys
    :postcondition: character fights the boss and either wins or loses
    :return: True if player defeats the boss, False otherwise

    >>> test_char = {"Current HP": 1000, "Level": 3, "Gold": 100, "Maximum HP": 200, "XP": 250}
    >>> execute_boss_fight(test_char)
    True
    """

    print("\n" + "=" * 80)
    print(RED + r"""

    ╔═══════════════════════════════════════════════════════════════════════╗
    ║                                                                       ║
    ║                    F I N A L   S H O W D O W N                        ║
    ║                                                                       ║
    ╚═══════════════════════════════════════════════════════════════════════╝

    """ + RESET)

    input(YELLOW + "Press Enter to face your destiny..." + RESET)

    print("\n" + RED + r"""
                  _______
                 /       \
                |  -   -  |
                |    V    |
                | (-----) |
                 \_______/
                    |||
                 ____|_____
                /          \
               |   ★ ★ ★   |
               |   SHERIFF  |
               |____________|
                  |      |
                  |      |
                 _|      |_
                |__|    |__|

               ☠ BLACKWOOD ☠
            "THE DEVIL WEARS A BADGE"

    """ + RESET)

    print(RED + "Sheriff Blackwood draws his revolver." + RESET)
    print(RED + "'The law has come for you, outlaw.  Time to hang. '" + RESET)

    boss = {"Name": "Sheriff Blackwood", "HP": 350, "Damage": 35}

    print("\n" + "=" * 80)
    print(f"{RED}BOSS HP: {boss['HP']}{RESET}  |  {GREEN}YOUR HP: {character['Current HP']}{RESET}")
    print("=" * 80)

    round_number = 0

    while character["Current HP"] > 0 and boss["HP"] > 0:
        round_number += 1
        print(f"\n{YELLOW}╔════ ROUND {round_number} ════╗{RESET}")

        if round_number % 2 == 0:
            print(CYAN + "💡 TIP: You can visit the shop [$] to buy health potions!" + RESET)

        print(f"\n{CYAN}[Enter] = Attack  |  [$] = Visit Shop{RESET}")
        action = input(CYAN + ">>> " + RESET).strip(). upper()

        if action == '$':
            print(YELLOW + "\nYou quickly duck behind cover and signal the shopkeeper!" + RESET)
            print(YELLOW + "The shopkeeper rushes over with his goods..." + RESET)
            shop_menu(character)
            print(YELLOW + "\nYou return to the fight!" + RESET)
            continue

        print(YELLOW + r"""

            YOU
             O
            /|\      💥 BANG! 
            / \     ════════>

        """ + RESET)

        player_damage = random.randint(35, 50)
        boss["HP"] -= player_damage

        print(GREEN + f"✓ Direct hit! You dealt {player_damage} damage to Blackwood!" + RESET)

        if boss["HP"] <= 0:
            print("\n" + GREEN + r"""

                    ╔═══════════════════════════╗
                    ║   BLACKWOOD DEFEATED!     ║
                    ╚═══════════════════════════╝

                              ___
                            _/   \_
                           /  X X  \
                          |    \_/   |
                           \  _____ /
                            \__|||__/
                               XXX
                              /   \
                             X     X

                    *THUD* He falls to the dust. 

            """ + RESET)

            print(GREEN + f"\nWith a final gasp, {boss['Name']} collapses." + RESET)
            print(GREEN + "Justice has been served.  Dusty Gulch is free!" + RESET)
            return True

        boss_hp_bar = "█" * (boss["HP"] // 8) + "░" * ((350 - boss["HP"]) // 8)
        print(f"\n{RED}Blackwood HP: [{boss_hp_bar}] {boss['HP']}/350{RESET}")

        input(YELLOW + "\nBlackwood returns fire!  Press Enter..." + RESET)

        print(RED + r"""

                            BLACKWOOD
                                O
            💥 BANG!           /|\
           <════════           / \

        """ + RESET)

        boss_damage = random.randint(30, 45)
        character["Current HP"] -= max(0, boss_damage)

        print(RED + f"✗ You took {boss_damage} damage!" + RESET)

        if character["Current HP"] <= 0:
            print("\n" + RED + r"""

                ╔═══════════════════════════════╗
                ║     Y O U   F A I L E D       ║
                ╚═══════════════════════════════╝

                         YOU
                          X
                         /|\    💀
                         / \

                *You collapse in the dust*

            """ + RESET)

            print(RED + "Your vision fades to black..." + RESET)
            print(RED + "Blackwood was too strong.  The corruption continues." + RESET)
            return False

        player_hp_bar = "█" * (character["Current HP"] // 10) + "░" * ((200 - character["Current HP"]) // 10)
        print(f"\n{GREEN}Your HP: [{player_hp_bar}] {character['Current HP']}/200{RESET}")

        print("\n" + "─" * 80)
        print(f"{RED}BLACKWOOD: {boss['HP']} HP{RESET}  |  {GREEN}YOU: {character['Current HP']} HP{RESET}  |  {YELLOW}GOLD: {character['Gold']}{RESET}")
        print("─" * 80)

    return False


def display_victory_ending(character: dict):
    honor = character. get("Honor", 0)
    gold = character.get("Gold", 0)

    if honor >= 50:
        print(YELLOW + r"""
╔════════════════════════════════════════════════════════════════════╗
║                                                                    ║
║        ░█████╗░  ██╗░░██╗███████╗██████╗░░█████╗░░░░███████╗       ║
║        ██╔══██╗  ██║░░██║██╔════╝██╔══██╗██╔══██╗░░██╔════╝        ║
║        ███████║  ███████║█████╗░░██████╔╝██║░░██║░░███████╗        ║
║        ██╔══██║  ██╔══██║██╔══╝░░██╔══██╗██║░░██║░░╚════██║        ║
║        ██║░░██║  ██║░░██║███████╗██║░░██║╚█████╔╝░░███████║        ║
║        ╚═╝░░╚═╝  ╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝░╚════╝░░░╚══════╝        ║
║                                                                    ║
║        ██╗░░░░░███████╗░██████╗░░█████╗░░█████╗░██╗░░░██╗          ║
║        ██║░░░░░██╔════╝██╔════╝░██╔══██╗██╔══██╗╚██╗░██╔╝          ║
║        ██║░░░░░█████╗░░██║░░██╗░███████║██║░░╚═╝░╚████╔╝░          ║
║        ██║░░░░░██╔══╝░░██║░░╚██╗██╔══██║██║░░██╗░░╚██╔╝░░          ║ 
║        ███████╗███████╗╚██████╔╝██║░░██║╚█████╔╝░░░██║░░░          ║
║        ╚══════╝╚══════╝░╚═════╝░╚═╝░░╚═╝░╚════╝░░░░╚═╝░░░          ║
║                                                                    ║
║    ════════════════════════════════════════════════════════════    ║
║                                                                    ║
║      Your name becomes a legend, a symbol of hope and justice.     ║
║                                                                    ║
║                                                                    ║
║                            ⚔️  ✨  ⚔️                             ║
║                                                                    ║
║                                ,^.                                 ║
║                               /   \                                ║
║                              | O O |                               ║
║                              |  >  |                               ║
║                              | ___ |                               ║
║                        ______|     |______                         ║
║                       |      \_____/      |                        ║
║                       |    /    |    \    |                        ║
║                       |___/_____|_____\___|                        ║
║                           |     |     |                            ║
║                           |     |     |                            ║
║                          /      |      \                           ║
║                        ,~  ,~_  |  _~,  ~,                         ║
║                      ,~   ( (') | (') )   ~,                       ║
║                    ,~     |  \_/ \_/  |     ~,                     ║
║                  ,~       |___________/       ~,                   ║
║                ,~    ___,/'           `\,___    ~,                 ║
║              ,~   ,/'                      `\,   ~,                ║
║            ,~   ,/'                            `\,  ~,             ║
║          ,~___/'__________________________________`\___~,          ║
║        ,'==============================================`,          ║
║        |         ⚔  THE FRONTIER'S GUARDIAN  ⚔          |          ║
║        |            "Justice Rides Eternal"             |          ║
║         `=============================================='           ║
║                                                                    ║
║            ✨ Your story will inspire generations ✨               ║
║                                                                    ║
╚════════════════════════════════════════════════════════════════════╝
""" + RESET)
        print(GREEN + f"You accumulated {gold} gold and donated it all to rebuild Dusty Gulch." + RESET)
        print(GREEN + "Your generosity is remembered forever." + RESET)

    else:
        print(RED + r"""
╔════════════════════════════════════════════════════════════════════╗
║                                                                    ║
║     ░█████╗░  ███████╗███████╗░█████╗░██████╗░███████╗██████╗░     ║
║     ██╔══██╗  ██╔════╝██╔════╝██╔══██╗██╔══██╗██╔════╝██╔══██╗     ║
║     ███████║  █████╗░░█████╗░░███████║██████╔╝█████╗░░██║░░██║     ║
║     ██╔══██║  ██╔══╝░░██╔══╝░░██╔══██║██╔══██╗██╔══╝░░██║░░██║     ║
║     ██║░░██║  ██║░░░░░███████╗██║░░██║██║░░██║███████╗██████╔╝     ║
║     ╚═╝░░╚═╝  ╚═╝░░░░░╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝╚══════╝╚═════╝░     ║
║                                                                    ║
║               ███╗░░██╗░█████╗░███╗░░░███╗███████╗                 ║
║               ████╗░██║██╔══██╗████╗░████║██╔════╝                 ║
║               ██╔██╗██║███████║██╔████╔██║█████╗░░                 ║
║               ██║╚████║██╔══██║██║╚██╔╝██║██╔══╝░░                 ║
║               ██║░╚███║██║░░██║██║░╚═╝░██║███████╗                 ║
║               ╚═╝░░╚══╝╚═╝░░╚═╝╚═╝░░░░░╚═╝╚══════╝                 ║
║                                                                    ║
║   ════════════════════════════════════════════════════════════     ║
║                                                                    ║
║       Your name is whispered in fear. You brought change,          ║
║                but through blood and fire.                         ║
║                                                                    ║
║                           ▲▲▲▲▲▲▲▲▲▲▲                              ║
║                         ▲▲░░░░░░░░░░░▲▲                            ║
║                       ▲▲░░██╗░░░░░██╗░░▲▲                          ║
║                     ▲▲░░░░███╗░░░███░░░░░▲▲                        ║
║                    ▲░░░░░░░███╗░███░░░░░░░░▲                       ║
║                   ▲░░░░░░░░░███████░░░░░░░░░▲                      ║
║                  ▲░░░░░░░░░░░░███░░░░░░░░░░░░▲                     ║
║                 ▲░░░░░░░░░░░░░░█░░░░░░░░░░░░░░▲                    ║
║                ▲░░░░░░░▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄░░░░░░░▲                   ║
║               ▲░░░░░░░█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█░░░░░░░▲                  ║
║              ▲░░░░░░░░█ ╔═══╗   ╔═══╗  █░░░░░░░░▲                  ║
║             ▲░░░░░░░░░█ ║ ◢ ║   ║ ◣ ║  █░░░░░░░░░▲                ║
║            ▲░░░░░░░░░░█ ╚═══╝   ╚═══╝  █░░░░░░░░░░▲                ║
║           ▲░░░░░░░░░░░█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█░░░░░░░░░░░▲              ║
║          ▲░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▲              ║
║         ▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲              ║
║                                                                    ║
║                🔥  A legend written in flames  🔥                  ║
║                                                                    ║
╚════════════════════════════════════════════════════════════════════╝
""" + RESET)
        print(YELLOW + f"You leave town with {gold} gold in your saddlebags." + RESET)
        print(YELLOW + "You are rich, but alone." + RESET)


def display_game_over():

    print(RED + r"""
╔════════════════════════════════════════════════════════════╗
║                                                            ║
║ ▓██   ██▓ ▒█████   █    ██     ▓█████▄  ██▓▓█████ ▓█████▄  ║
║  ▒██  ██▒▒██▒  ██▒ ██  ▓██▒    ▒██▀ ██▌▓██▒▓█   ▀ ▒██▀ ██▌ ║
║   ▒██ ██░▒██░  ██▒▓██  ▒██░    ░██   █▌▒██▒▒███   ░██   █▌ ║
║   ░ ▐██▓░▒██   ██░▓▓█  ░██░    ░▓█▄   ▌░██░▒▓█  ▄ ░▓█▄   ▌ ║
║   ░ ██▒▓░░ ████▓▒░▒▒█████▓     ░▒████▓ ░██░░▒████▒░▒████▓  ║
║    ██▒▒▒ ░ ▒░▒░▒░ ░▒▓▒ ▒ ▒      ▒▒▓  ▒ ░▓  ░░ ▒░ ░ ▒▒▓  ▒  ║
║  ▓██ ░▒░   ░ ▒ ▒░ ░░▒░ ░ ░      ░ ▒  ▒  ▒ ░ ░ ░  ░ ░ ▒  ▒  ║
║  ▒ ▒ ░░  ░ ░ ░ ▒   ░░░ ░ ░      ░ ░  ░  ▒ ░   ░    ░ ░  ░  ║
║  ░ ░         ░ ░     ░            ░     ░     ░  ░   ░     ║
║  ░ ░                            ░                  ░       ║
║                                                            ║
║    The frontier is unforgiving. Your journey ends here.    ║
║                                                            ║
║                         ___________                        ║
║                       ,'           `.                      ║
║                      /   ╔═══════╗   \                     ║
║                     |    ║       ║    |                    ║
║                     |    ║ X   X ║    |                    ║
║                     |    ║       ║    |                    ║
║                     |    ║   o   ║    |                    ║
║                     |    ║       ║    |                    ║
║                     |    ║  ___  ║    |                    ║
║                      \   ╚═══════╝   /                     ║
║                       `.___________,'                      ║
║                      __|___________|__                     ║
║                      /  ═══════════  \                     ║
║                     |      R.I.P.     |                    ║
║                     |    HERE LIES    |                    ║
║                     |    A WANDERER   |                    ║
║                      \_______________/                     ║
║                                                            ║
║                                                            ║
║                                                            ║
╚════════════════════════════════════════════════════════════╝
""" + RESET)


def get_player_name() -> str:
    while True:
        name = input(BLUE + "Enter your outlaw's name >>> " + RESET).strip()
        if name:
            return name
        print("A name has power. You must have one.")


def game_loop(board_rows: int, board_columns: int, encounter_chance: int):
    """
    Execute the main game loop.

    :param board_rows: number of rows in the game board
    :param board_columns: number of columns in the game board
    :param encounter_chance: percentage chance of encounter per move
    :precondition: board_rows, board_columns, encounter_chance are integers
    :postcondition: runs the complete game from start to finish
    :return: None
    """

    board = make_board(board_rows, board_columns)

    banner = """
    ╔═════════════════════════════════════════════════════════════════════════════════════════════════╗
    ║                                                                                                 ║
    ║                                                                                                 ║
    ║                        ▒█████   █    ██ ▄▄▄█████▓ ██▓    ▄▄▄       █     █░                     ║
    ║                       ▒██▒  ██▒ ██  ▓██▒▓  ██▒ ▓▒▓██▒   ▒████▄    ▓█░ █ ░█░                     ║
    ║                       ▒██░  ██▒▓██  ▒██░▒ ▓██░ ▒░▒██░   ▒██  ▀█▄  ▒█░ █ ░█                      ║
    ║                       ▒██   ██░▓▓█  ░██░░ ▓██▓ ░ ▒██░   ░██▄▄▄▄██ ░█░ █ ░█                      ║
    ║                       ░ ████▓▒░▒▒█████▓   ▒██▒ ░ ░██████▒▓█   ▓██▒░░██▒██▓                      ║
    ║                       ░ ▒░▒░▒░ ░▒▓▒ ▒ ▒   ▒ ░░   ░ ▒░▓  ░▒▒   ▓▒█░░ ▓░▒ ▒                       ║
    ║                         ░ ▒ ▒░ ░░▒░ ░ ░     ░    ░ ░ ▒  ░ ▒   ▒▒ ░  ▒ ░ ░                       ║
    ║                       ░ ░ ░ ▒   ░░░ ░ ░   ░        ░ ░    ░   ▒     ░   ░                       ║
    ║                           ░ ░     ░                  ░  ░     ░  ░    ░                         ║
    ║                                                                                                 ║
    ║        ██▀███  ▓█████ ▓█████▄ ▓█████ ███▄ ▄███▓ ██▓███  ▄▄▄█████▓ ██▓ ▒█████   ███▄    █        ║
    ║       ▓██ ▒ ██▒▓█   ▀ ▒██▀ ██▌▓█   ▀▓██▒▀█▀ ██▒▓██░  ██▒▓  ██▒ ▓▒▓██▒▒██▒  ██▒ ██ ▀█   █        ║
    ║       ▓██ ░▄█ ▒▒███   ░██   █▌▒███  ▓██    ▓██░▓██░ ██▓▒▒ ▓██░ ▒░▒██▒▒██░  ██▒▓██  ▀█ ██▒       ║
    ║       ▒██▀▀█▄  ▒▓█  ▄ ░▓█▄   ▌▒▓█  ▄▒██    ▒██ ▒██▄█▓▒ ▒░ ▓██▓ ░ ░██░▒██   ██░▓██▒  ▐▌██▒       ║
    ║       ░██▓ ▒██▒░▒████▒░▒████▓ ░▒████▒██▒   ░██▒▒██▒ ░  ░  ▒██▒ ░ ░██░░ ████▓▒░▒██░   ▓██░       ║
    ║       ░ ▒▓ ░▒▓░░░ ▒░ ░ ▒▒▓  ▒ ░░ ▒░ ░ ▒░   ░  ░▒▓▒░ ░  ░  ▒ ░░   ░▓  ░ ▒░▒░▒░ ░ ▒░   ▒ ▒        ║
    ║         ░▒ ░ ▒░ ░ ░  ░ ░ ▒  ▒  ░ ░  ░  ░      ░░▒ ░         ░     ▒ ░  ░ ▒ ▒░ ░ ░░   ░ ▒░       ║
    ║         ░░   ░    ░    ░ ░  ░    ░  ░      ░   ░░         ░       ▒ ░░ ░ ░ ▒     ░   ░ ░        ║
    ║          ░        ░  ░   ░       ░  ░      ░                       ░      ░ ░           ░       ║
    ║                        ░                                                                        ║
    ║                                                                                                 ║
    ║                               🌵  A Tale of Justice and Vengeance  🌵                           ║
    ║                                                                                                 ║
    ╚═════════════════════════════════════════════════════════════════════════════════════════════════╝
        """
    print(YELLOW + banner + RESET)

    print("\n" + "═" * 90)
    print(CYAN + "                                  THE STORY" + RESET)
    print("═" * 90)
    print("""
        ┌─────────────────────────────────────────────────────────────────────┐
        │                                                                     │
        │  The year is 1885. The Wild West bleeds its final breaths.          │
        │                                                                     │
        │  Sheriff Blackwood rules Dusty Gulch with an iron fist and a        │
        │  heart of stone. His corruption has poisoned the land. Innocent     │
        │  blood stains the gallows. The law has become the outlaw.           │
        │                                                                     │
        │  You are a wanderer—haunted by a dark past, seeking redemption...   │
        │  or revenge. Your path is yours to carve.                           │
        │                                                                     │
        │  Will you be the hero this land desperately needs?                  │
        │  Or will you become the nightmare Blackwood fears?                  │
        │                                                                     │
        │  The frontier awaits your answer, stranger.                         │
        │                                                                     │
        └─────────────────────────────────────────────────────────────────────┘
        """)

    print("═" * 90)
    print(GREEN + "                               🎯 HOW TO WIN" + RESET)
    print("═" * 90)
    print("""
        Victory demands three trials:

        ┌───────────────────────────────────────────────────────────────────┐
        │ 1. ⚔️  GAIN EXPERIENCE                                            │
        │    • Battle enemies, make choices, solve deadly puzzles           │
        │    • Reach Level 3 (250 total XP required)                        │
        │    • Each decision shapes your legend                             │
        │                                                                   │
        │ 2. 🏰 REACH THE FORTRESS                                          │
        │    • Navigate to coordinates (9, 9) - the southeast corner        │
        │    • Use [M] to view your map and track progress                  │
        │    • The final battle awaits at Blackwood's stronghold            │
        │                                                                   │
        │ 3. 💀 DEFEAT SHERIFF BLACKWOOD                                    │
        │    • Only Level 3 warriors can challenge him                      │
        │    • The boss fight triggers automatically at (9, 9)              │
        │    • Bring justice... or bring hell                               │
        └───────────────────────────────────────────────────────────────────┘
        """)

    print("═" * 90)
    print(BLUE + "                            💡 SURVIVAL TIPS" + RESET)
    print("═" * 90)
    print("""
        ┌───────────────────────────────────────────────────────────────────┐
        │  ★  Don't rush to (9,9) - Level up first or die trying!          │
        │  ★  Hoard gold for healing potions - they save lives             │
        │  ★  Visit the shop [$] before the boss fight                     │
        │  ★  Honorable choices reward more XP                             │
        │  ★  You can shop DURING the boss fight - use it wisely!          │
        │  ★  Keep HP above 100 before entering (9,9)                      │
        │  ★  Every choice matters - honor or fear, hero or villain        │
        └───────────────────────────────────────────────────────────────────┘
        """)

    print("\n" + "═" * 90)
    print(RED + "                         ⚡ THE FRONTIER AWAITS, STRANGER ⚡" + RESET)
    print("═" * 90 + "\n")

    player_name = get_player_name()
    character = make_character(player_name)
    achieved_goal = False

    print(YELLOW + f"\n   Welcome, {player_name}. Your legend begins... now.\n" + RESET)
    print(GREEN + "   🌵 ════════════════════════════════════════════════════ 🌵\n" + RESET)

    while is_alive(character) and not achieved_goal:
        print("\n\n\n\n" + "~" * 100)
        print(get_location_description(board, character["X-coordinate"], character["Y-coordinate"]))
        print(BLUE + f"\nLocation: ({character['X-coordinate']}, {character['Y-coordinate']})" + RESET)
        print(YELLOW + f"💰 Gold: {character['Gold']}" + RESET)

        choice = get_user_choice()

        if check_cheat_code(choice, character):
            continue

        if choice == 'Q':
            print("The frontier will wait.  For now.")
            break

        elif choice == 'I':
            display_character_stats(character)

        elif choice == 'M':
            display_map(board_rows, board_columns, character["X-coordinate"], character["Y-coordinate"])

        elif choice == '$':
            print(CYAN + "\n🏪 You enter the General Store..." + RESET)
            shop_menu(character)

        elif choice in ['N', 'S', 'E', 'W']:
            if validate_move(board, character, choice):
                move_character(character, choice)
                print(f"You travel {choice}...")

                if check_for_challenges(encounter_chance):
                    encounter_type = determine_encounter_type()

                    if encounter_type == "combat" and character["Current HP"] < 100:
                        print(YELLOW + "\n💡 TIP: You look wounded. Visit the shop [$] to heal before fighting!" + RESET)

                    survived = execute_challenge_protocol(character, encounter_type)
                    if not survived:
                        display_game_over()
                        return

                if character_has_leveled(character):
                    level_up_character(character)
                    print(MAGENTA + "\n[ L E V E L   U P !  ]" + RESET)
                    print(f"You feel stronger.  You are now Level {character['Level']}!")

                is_at_goal_location = (character["X-coordinate"] == board_columns - 1 and
                                       character["Y-coordinate"] == board_rows - 1)

                if is_at_goal_location and character["Level"] >= 3:
                    print(YELLOW + "\n" + "=" * 80 + RESET)
                    print(YELLOW + "You've reached Sheriff Blackwood's fortress!" + RESET)
                    print(YELLOW + f"Your HP: {character['Current HP']}/{character['Maximum HP']}" + RESET)
                    print(YELLOW + f"Your Gold: {character['Gold']}" + RESET)
                    print(YELLOW + "=" * 80 + RESET)


                    print(CYAN + "\n💡 Tip: Visit the shop [$] before the final fight!" + RESET)
                    final_choice = input(CYAN + "Enter the fortress now?  [Y/N] or [$] for shop >>> " + RESET).strip(). upper()

                    if final_choice == '$':
                        print(YELLOW + "You visit the shop one last time..." + RESET)
                        shop_menu(character)
                        print(YELLOW + "\nReady for the final battle?" + RESET)
                        final_choice = input(CYAN + "Enter the fortress?  [Y/N] >>> " + RESET).strip().upper()

                    if final_choice == 'Y':
                        boss_defeated = execute_boss_fight(character)
                        if boss_defeated:
                            achieved_goal = True
                        elif not is_alive(character):
                            display_game_over()
                            return
                    else:
                        print(YELLOW + "You step back.  You can enter when ready." + RESET)
                        character["X-coordinate"] -= 1
            else:

                print(RED + "⚠️  You're at the edge of a cliff!  You cannot go that direction." + RESET)
                print(YELLOW + "The ground drops away into darkness.  Turn back." + RESET)
        else:
            print("A strange wind blows.  That command means nothing here.")

    if achieved_goal:
        display_victory_ending(character)
    elif not is_alive(character):
        display_game_over()


def main():
    """
    Drive the program.
    """
    print(CYAN + "\n" + "=" * 80)
    print("OUTLAW'S REDEMPTION - ENDING VIEWER")
    print("=" * 80 + RESET)
    print("\nSelect an ending to view:\n")
    print("1. Hero Ending (High Honor)")
    print("2. Feared Ending (Low Honor)")
    print("3. Game Over (Death)")

    choice = input(YELLOW + "\nEnter choice (1-3): " + RESET).strip()

    if choice == "1":
        print(GREEN + "\n[Hero Ending - High Honor Path]" + RESET)
        test_character = {
            "Name": "The Hero",
            "Honor": 80,
            "Gold": 500
        }
        input("\nPress Enter to view...")
        display_victory_ending(test_character)

    elif choice == "2":
        print(RED + "\n[Feared Ending - Low Honor Path]" + RESET)
        test_character = {
            "Name": "The Outlaw",
            "Honor": 20,
            "Gold": 800
        }
        input("\nPress Enter to view...")
        display_victory_ending(test_character)

    elif choice == "3":
        print(RED + "\n[Game Over - Death]" + RESET)
        input("\nPress Enter to view...")
        display_game_over()

    else:
        print("Invalid choice.")


if __name__ == "__main__":
    main()