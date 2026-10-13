"""
Ryan Yarali

Manages random encounters including honor choices, combat, and puzzles.
"""
import random
from combat import execute_combat_encounter
from character import gain_xp
from color import *

def check_for_challenges(encounter_chance: int) -> bool:
    """
    Determine if an encounter occurs based on chance percentage.

    :param encounter_chance: percentage chance of encounter (0-100)
    :precondition: encounter_chance must be an integer between 0 and 100
    :postcondition: randomly determines if encounter occurs
    :return: True if encounter occurs, False otherwise

    >>> random.seed(1)
    >>> check_for_challenges(100)
    True
    """
    return random.randint(1, 100) <= encounter_chance


def determine_encounter_type() -> str:
    """
    Randomly select an encounter type.

    :precondition: none
    :postcondition: randomly selects one of three encounter types
    :return: string representing encounter type ('honor', 'combat', or 'puzzle')

    >>> random. seed(1)
    >>> determine_encounter_type()
    'honor'
    """
    roll = random.randint(1, 100)
    if roll <= 35:
        return "honor"
    elif roll <= 75:
        return "combat"
    else:
        return "puzzle"


def execute_honor_choice(character: dict) -> int:
    """
    Present a moral choice and return the XP gained.

    :param character: a dictionary representing the player character
    :precondition: character must have Honor and Gold keys
    :postcondition: modifies character's honor and gold based on choice
    :return: integer XP gained

    >>> test_char = {"Honor": 0, "Gold": 50}
    >>> execute_honor_choice(test_char)
    25
    """
    scenarios = [
        {
            "desc": "You find a wounded traveler bleeding on the road.  They beg for help.",
            "opts": [
                {"txt": "Help them and share your medical supplies", "honor": 15, "xp": 25, "gold": -10},
                {"txt": "Rob them while they're defenseless", "honor": -25, "xp": 10, "gold": 40},
                {"txt": "Walk away without getting involved", "honor": -5, "xp": 5, "gold": 0}
            ]
        },
        {
            "desc": "A shopkeeper accuses a starving child of stealing bread.",
            "opts": [
                {"txt": "Pay for the bread and defend the child", "honor": 20, "xp": 30, "gold": -15},
                {"txt": "Help the shopkeeper chase the child away", "honor": -15, "xp": 10, "gold": 5},
                {"txt": "Ignore the situation and walk away", "honor": -10, "xp": 5, "gold": 0}
            ]
        },
        {
            "desc": "You witness a stagecoach robbery in progress.  Three bandits attack innocent passengers.",
            "opts": [
                {"txt": "Intervene heroically and defend the passengers", "honor": 30, "xp": 40, "gold": -5},
                {"txt": "Join the bandits for a share of the loot", "honor": -30, "xp": 15, "gold": 80},
                {"txt": "Hide and wait for it to end", "honor": -15, "xp": 5, "gold": 0}
            ]
        },
        {
            "desc": "A desperate farmer offers you his last horse in exchange for protection from bandits.",
            "opts": [
                {"txt": "Protect his family for free, refusing payment", "honor": 25, "xp": 35, "gold": 0},
                {"txt": "Take the horse and leave them to their fate", "honor": -20, "xp": 10, "gold": 50},
                {"txt": "Negotiate a fair price and provide protection", "honor": 10, "xp": 25, "gold": 25}
            ]
        },
        {
            "desc": "You find a wanted poster offering $200 for a young woman accused of murder.  She claims she's innocent.",
            "opts": [
                {"txt": "Believe her story and help her escape", "honor": 20, "xp": 30, "gold": 0},
                {"txt": "Turn her in for the bounty", "honor": -25, "xp": 15, "gold": 200},
                {"txt": "Let her go but keep your distance", "honor": 5, "xp": 10, "gold": 0}
            ]
        },
        {
            "desc": "A dying outlaw offers you a map to hidden gold if you promise to deliver a letter to his daughter.",
            "opts": [
                {"txt": "Promise to deliver the letter honorably", "honor": 20, "xp": 30, "gold": 100},
                {"txt": "Take the map and burn the letter", "honor": -30, "xp": 15, "gold": 150},
                {"txt": "Refuse both the map and the request", "honor": 0, "xp": 5, "gold": 0}
            ]
        },
        {
            "desc": "You catch a young boy trying to steal your horse. He says his sister is sick and needs medicine.",
            "opts": [
                {"txt": "Give him gold for medicine and let him go", "honor": 30, "xp": 40, "gold": -50},
                {"txt": "Beat him as a lesson and send him away", "honor": -25, "xp": 10, "gold": 0},
                {"txt": "Take him to buy medicine yourself", "honor": 35, "xp": 45, "gold": -40}
            ]
        },
        {
            "desc": "You find a lockbox that fell from a bank wagon. It contains $500 in gold.",
            "opts": [
                {"txt": "Return it to the bank honestly", "honor": 30, "xp": 35, "gold": 50},
                {"txt": "Keep the gold.  Finders keepers.", "honor": -25, "xp": 10, "gold": 500},
                {"txt": "Take half and return half", "honor": -5, "xp": 15, "gold": 250}
            ]
        },
        {
            "desc": "You witness a public hanging of a man who claims he was framed by Sheriff Blackwood.",
            "opts": [
                {"txt": "Cause a distraction and help him escape", "honor": 30, "xp": 40, "gold": -20},
                {"txt": "Do nothing. It's not your fight.", "honor": -20, "xp": 5, "gold": 0},
                {"txt": "Join the crowd and watch justice be served", "honor": -25, "xp": 5, "gold": 10}
            ]
        },
        {
            "desc": "A group of children beg you to rescue their teacher who was kidnapped by bandits.",
            "opts": [
                {"txt": "Mount a rescue mission immediately", "honor": 35, "xp": 50, "gold": -15},
                {"txt": "Tell them to ask someone else", "honor": -20, "xp": 5, "gold": 0},
                {"txt": "Offer to negotiate with the bandits instead", "honor": 15, "xp": 30, "gold": -30}
            ]
        }
    ]

    scenario = random.choice(scenarios)
    print(YELLOW + "\n[ C H O I C E ]" + RESET)
    print(YELLOW + f"\n{scenario['desc']}" +RESET)
    for index, option in enumerate(scenario["opts"], 1):
        print(YELLOW + f"  {index}. {option['txt']}" + RESET)

    choice = 0
    while choice not in [1, 2, 3]:
        try:
            choice = int(input(BLUE +"What do you do? (1-3) >>> " + RESET))
        except ValueError:
            print("Invalid input.")

    selected = scenario["opts"][choice - 1]
    character["Honor"] += selected["honor"]
    character["Gold"] = max(0, character["Gold"] + selected["gold"])
    print(GREEN + f"Your choice has been made.  You gained {selected['xp']} XP and {selected['honor']} Honor." + RESET)
    return selected['xp']


def execute_puzzle(character: dict) -> int:
    """
    Present a puzzle and return the XP gained.

    :param character: a dictionary representing the player character
    :precondition: character must have Gold key
    :postcondition: may increase gold if puzzle solved
    :return: integer XP gained

    >>> test_char = {"Gold": 50}
    >>> execute_puzzle(test_char)
    35
    """
    puzzles = [
        {
            "q": "I have cities, but no houses. I have mountains, but no trees. I have water, but no fish. What am I?",
            "a": "map"
        },
        {
            "q": "I speak without a mouth and hear without ears. I have no body, but I come alive with wind. What am I?",
            "a": "echo"
        },
        {
            "q": "The more you take, the more you leave behind. What am I?",
            "a": "footsteps"
        },
        {
            "q": "What can travel around the world while staying in a corner?",
            "a": "stamp"
        },
        {
            "q": "I have a head and a tail, but no body. What am I?",
            "a": "coin"
        },
        {
            "q": "What gets wetter the more it dries? ",
            "a": "towel"
        },
        {
            "q": "What can run but never walks, has a mouth but never talks, has a bed but never sleeps?",
            "a": "river"
        },
        {
            "q": "I am not alive, but I grow. I don't have lungs, but I need air. What am I?",
            "a": "fire"
        },
        {
            "q": "I fly without wings. I cry without eyes.  Wherever I go, darkness follows me. What am I?",
            "a": "cloud"
        },
        {
            "q": "I'm tall when I'm young, and I'm short when I'm old. What am I?",
            "a": "candle"
        }
    ]

    puzzle = random.choice(puzzles)
    print(YELLOW + "\n[ R I D D L E ]" + RESET)
    print(YELLOW + f"\nA mysterious old prospector poses a riddle:\n'{puzzle['q']}'" +RESET)
    answer = input(BLUE + "Your answer >>> " + RESET).strip(). lower()

    if answer == puzzle['a']:
        print(GREEN + "The old man grins.  'Correct!' He tosses you a small pouch of gold." + RESET)
        character["Gold"] += 50
        return 35
    else:
        print(YELLOW + f"The old man shakes his head.  'Nope. The answer was... {puzzle['a']}.'" + RESET)
        return 10


def execute_challenge_protocol(character: dict, encounter_type: str) -> bool:
    """
    Execute the appropriate challenge based on encounter type.

    :param character: a dictionary representing the player character
    :param encounter_type: string representing the type of encounter
    :precondition: encounter_type must be 'honor', 'combat', or 'puzzle'
    :postcondition: executes an encounter and modifies character
    :return: True if character survives, False if character dies

    >>> test_char = {"Level": 1, "Current HP": 100, "Gold": 50, "Honor": 0, "XP": 0}
    >>> execute_challenge_protocol(test_char, 'puzzle')
    True
    """
    if encounter_type == "combat":
        victory, xp_gained = execute_combat_encounter(character)
        gain_xp(character, xp_gained)
        return victory
    elif encounter_type == "honor":
        xp_gained = execute_honor_choice(character)
        gain_xp(character, xp_gained)
        return True
    elif encounter_type == "puzzle":
        xp_gained = execute_puzzle(character)
        gain_xp(character, xp_gained)
        return True
    return True