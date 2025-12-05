"""
Ryan Yarali
A01464263

Handles enemy generation, damage calculation and combat mechanics.
"""
import random


def generate_enemy(player_level: int) -> dict:
    """
    Generate an enemy dictionary scaled to the player level.

    :param player_level: the current level of the player character
    :precondition: player_level must be a positive integer
    :postcondition: creates an enemy dictionary with randomized stats
    :return: dictionary representing an enemy

    >>> enemy = generate_enemy(1)
    >>> enemy['Name']
    'Bandit'
    """
    enemy_types = {
        1: {"name": "Bandit", "hp": (30, 50), "dmg": (8, 15), "gold": (10, 25)},
        2: {"name": "Outlaw", "hp": (60, 80), "dmg": (12, 20), "gold": (30, 50)},
        3: {"name": "Gunslinger", "hp": (90, 120), "dmg": (20, 35), "gold": (50, 80)},
    }
    template = enemy_types.get(player_level, enemy_types[1])
    return {
        "Name": template["name"],
        "HP": random.randint(*template["hp"]),
        "Damage": random.randint(*template["dmg"]),
        "Gold": random.randint(*template["gold"]),
    }


def execute_combat_encounter(character: dict) -> tuple:
    """
    Execute a complete combat encounter.

    :param character: a dictionary representing the player character
    :precondition: character must have Level, Current HP, and Gold keys
    :postcondition: character may take damage, gain gold, or die
    :return: tuple of (victory_boolean, xp_gained)

    >>> test_char = {"Level": 1, "Current HP": 1000, "Gold": 0, "XP": 0}
    >>> victory, xp = execute_combat_encounter(test_char)
    >>> victory
    True
    """
    player_level = character.get("Level", 1)
    enemy = generate_enemy(player_level)
    xp_reward = 20 + (player_level * 5)

    print("\n*<[ C O M B A T ]>*")
    print(f"\nA wild {enemy['Name']} appears!")

    while character["Current HP"] > 0 and enemy["HP"] > 0:
        print(f"\nYour HP: {character['Current HP']} | Enemy HP: {enemy['HP']}")
        input("Press Enter to attack...")

        player_damage = random.randint(10 + player_level * 5, 20 + player_level * 5)
        enemy["HP"] -= player_damage
        print(f"You attack, dealing {player_damage} damage!")

        if enemy["HP"] <= 0:
            print(f"You defeated the {enemy['Name']}!")
            character["Gold"] += enemy["Gold"]
            print(f"You loot {enemy['Gold']} gold and gain {xp_reward} XP.")
            return True, xp_reward

        enemy_damage = random.randint(enemy["Damage"] - 5, enemy["Damage"] + 5)
        character["Current HP"] -= max(0, enemy_damage)
        print(f"The {enemy['Name']} retaliates, dealing {enemy_damage} damage to you!")

        if character["Current HP"] <= 0:
            print("You have been defeated...")
            return False, 0

    return False, 0