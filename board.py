"""
Ryan Yarali
A01464263

Board module.
"""


def generate_coordinates(rows: int, columns: int) -> list:
    """
    Generate all (row, column) coordinates for a grid.

    :param rows: number of rows in the grid
    :param columns: number of columns in the grid
    :precondition: rows must be a positive integer
    :precondition: columns must be a positive integer
    :postcondition: returns a list of all coordinate tuples in the grid
    :return: list of (row, column) tuples

    >>> generate_coordinates(2, 3)
    [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2)]
    >>> len(generate_coordinates(10, 10))
    100
    """
    return [(row, column) for row in range(rows) for column in range(columns)]


def generate_unique_room_descriptions() -> list:
    """
    Generate 100 completely unique room descriptions.

    :precondition: none
    :postcondition: returns exactly 100 unique room descriptions
    :return: list of 100 unique room description strings

    >>> descriptions = generate_unique_room_descriptions()
    >>> len(descriptions)
    100
    """
    return [
        # === ROW 0 (Y=0): THE SCORCHED FRONTIER ===
        "Endless desert stretches before you. Heat shimmers off the cracked earth like water. A sun-bleached skull grins up from the sand, half-buried by time and wind. Behind you lies a burning past. Ahead: redemption... or revenge.",
        "A shattered wagon wheel lies abandoned. 'MURPHY FAMILY - 1881' is carved into the weathered wood. Scattered belongings tell a tragic story - toys, letters, a family portrait. They never made it to California.",
        "The dry rocks are alive with movement. Coiled serpents sun themselves, their rattles creating a symphony of warning. The sound says 'GO BACK'. Only fools ignore the wisdom of serpents.",
        "Once this was a river full of life. Now only sun-bleached bones remain in the dust. Animal or human? Does it matter? Death looks the same in the desert. The creek bed remembers better days.",
        "Towering rock formations provide blessed relief from the merciless sun. Ancient handprints cover the stone walls, left by people who walked here a thousand years ago. This place has witnessed empires rise and fall.",
        "A weathered wooden cross marks a nameless grave. Fresh wildflowers rest against it. Who brings them in this wasteland? Someone who loved. Someone who remembers. Or someone burdened by guilt.",
        "Mountains of tumbleweeds pile against rusted barbed wire. Four trails meet here, all leading nowhere. The wire fence marks boundaries that no longer exist. A monument to abandonment.",
        "A rusted pickaxe stands embedded in stone. The faded claim notice reads 'THIS LAND IS MINE - GOLD OR DEATH'. Bullet holes perforate the sign. Looks like the prospector got death instead of gold.",
        "A solitary Joshua tree stands defiant against the wasteland. Hearts carved in its bark: 'Maria + John 4EVER'. But forever ended long ago. The tree remembers their promises.",
        "Centuries of sandblasting wind have sculpted these rocks into twisted shapes. Some look like screaming faces. Others like reaching hands. The wind howls through gaps, carrying ancient warnings.",

        # === ROW 1 (Y=1): DUSTY GULCH - THE GHOST TOWN ===
        "A bullet-riddled sign proclaims 'DUSTY GULCH - Pop: 247'. But the numbers have been crossed out repeatedly: 246... 245... 244... Someone stopped counting. Welcome to hell.",
        "The General Store's windows are boarded, the door hanging by one hinge. Inside: empty shelves, scattered coins, broken dreams. The ledger's last entry: 'They took everything. God help us.' God didn't listen.",
        "The blacksmith's forge is cold. The anvil sits silent, hammer dropped mid-swing. Horseshoes rust on the wall. A half-finished sword lies abandoned. The smith fled from something terrible.",
        "A horse trough, miraculously full of clean water. Three horses drink lazily. One is saddled, but its rider is nowhere to be seen. There are dark stains on the leather saddle.",
        "The town square is dominated by a grim gallows. Thirteen steps lead to the platform. A noose sways in the breeze. Thirteen names are carved below it. A fresh carving says 'TOMORROW: YOU'.",
        "The chapel's white paint is peeling like sunburnt skin. Pews are overturned, hymnals scattered. 'Father, forgive them' is written in the dust on the altar. But God has left this town.",
        "The saloon's back alley is a testament to violence. Broken whiskey bottles, bloodstains of varying ages, and old poker cards. Wanted posters are plastered on the walls. Your face isn't among them. Yet.",
        "The old livery stable smells of hay and fear. The horses whinny nervously as you approach. They sense death on the wind. A map is pinned to the wall with a knife, an 'X' marking the sheriff's office.",
        "The old sheriff's office has been ransacked. The desk is overturned, files scattered like snow. The jail cell door has been torn from its hinges. 'BLACKWOOD WAS HERE' is scratched deep into the stone wall.",
        "You stand on a residential street lined with silent homes. No children play. No smoke rises from chimneys. Every curtain is drawn tight. This is a town that holds its breath, waiting for the next tragedy.",

        # === ROW 2 (Y=2): THE ABANDONED HOMESTEADS ===
        "The Harper Homestead's door swings on rusty hinges, creaking a lonely song. A family portrait lies on the floor, its glass shattered. The dinner table is set for a meal that was never eaten. 'They came at midnight' is scrawled on the wall.",
        "A child's yard, frozen in time. A wooden rocking horse sits motionless. A handmade doll with button eyes stares blankly at the sky. Tiny footprints lead away from the house, and then just... stop.",
        "An old wishing well. The rope is frayed, the bucket long gone. You drop a stone and hear no splash, no sound at all. How deep does it go? Deep enough to hide secrets.",
        "Two identical houses face each other across the dusty path, a mirror of misery. The same broken windows, the same decaying porches. It's said two brothers lived here, rivals to the end. They died staring at each other's failure.",
        "A once-beautiful garden is now a wild, thorny jungle. Roses grow through the slats of a broken picket fence. Their thorns are like barbed wire. A reminder that even beauty can become dangerous.",
        "A rocking chair on a porch moves back and forth, creaking rhythmically. But there is no wind. And no one is sitting in it. When you look directly at it, it stops. When you look away, the creaking resumes.",
        "A laundry line is strung between two poles. Clothes hang stiff and faded, bleached by a thousand suns. A man's shirt, a woman's dress, a small child's pants. A family snapshot, captured in cloth and time.",
        "An empty dog house with 'RUSTY' carved above the door. The chain lies coiled and empty, the collar still attached. There are deep scratch marks on the inside of the door. Rusty wanted out. Badly.",
        "A white picket fence, the symbol of a peaceful life, is now broken and leaning. Wild roses, untamed and beautiful, push through the gaps. Someone dreamed of a quiet life here. Dreams don't stop the desert.",
        "The one-room schoolhouse is eerily silent. The alphabet is still on the chalkboard. Tiny desks sit in crooked rows. An open textbook displays 'Chapter 7: The Nature of Justice'. A lesson that was never finished.",

        # === ROW 3 (Y=3): THE RED ROCK BADLANDS ===
        "You enter a canyon where the rock walls tower 300 feet high, glowing crimson in the sun. Your voice echoes for miles. A low rumble of thunder is heard, but the sky is clear. The ancients are speaking.",
        "This is Ambush Narrows, a tight pass between cliffs. Boulders are balanced precariously above, ready to fall. Dried bloodstains on the stone are a testament to the many who entered but never left.",
        "A sheer cliff face is covered in thousand-year-old petroglyphs. They depict hunters, warriors, and dying men. One symbol repeats over and over: a skull. This was not art; it was a warning.",
        "You find a sacred spring. Crystal-clear water bubbles up from the earth into a stone basin carved by an ancient people. The water is cold, pure, and life-giving. For a moment, you are safe.",
        "You enter a forest of silent giants. Saguaro cacti, 40 feet tall, stand with their arms raised to the sky like frozen sentinels. One of them has a door carved into its side. Do you dare to look inside?",
        "The entrance to Echo Cave is a maw of absolute darkness. You hear only the drip... drip... drip of water. You call out, 'Hello?' A voice that is not your own whispers back, '...help me...'",
        "The ground is littered with the fossilized bones of creatures from a lost world. Skeletons of immense beasts are embedded in the rock. A humbling reminder that time makes fools of even the mightiest.",
        "You stand atop a high mesa, a flat-topped mountain with a 360-degree view. You can see for 50 miles in every direction. Nothing can hide from you up here. But you can't hide either.",
        "You push through a thicket of dense, thorny chaparral. It's hard to walk and easy to get lost. You hear rattling from every direction. You can't see your own feet. Watch every single step.",
        "You've entered a box canyon. Sheer rock walls on three sides. No exit. It's a perfect place to hide. It's also a perfect trap. The only question is: are you the hunter, or the prey?",

        # === ROW 4 (Y=4): THE GOLD RUSH GRAVEYARD ===
        "The entrance to Mine Shaft Alpha is boarded up. A sign, riddled with bullet holes, reads 'DANGER - KEEP OUT'. Local legend says 40 miners went in after a fabled vein of gold. None came out.",
        "A mountain of tailings, crushed rock discarded from the mines, looms over you. It represents years of back-breaking labor and desperate dreams. A monument to the madness that gold inspires.",
        "The remains of a tent city, where hundreds of miners once lived. Now there are only rotted canvas and broken poles. A diary lies open in the dirt: 'Day 93. No gold. No food. No hope.' Day 94 is blank.",
        "A graveyard of abandoned sluice boxes lines a dry riverbed. It seems everyone left in a hurry, mid-pan. Did they all strike it rich and leave? Or did something find them first?",
        "The ground is a forest of wooden claim stakes. Every stake has a name, and every name is crossed out, replaced by another. 'MURPHY - NO TRESPASSING' has been shot through. Property is a deadly argument here.",
        "This mine shaft collapsed years ago, sealing its secrets forever. The splintered ends of pickaxes are visible in the rubble. They say the miners are still in there, guarding their gold for eternity.",
        "The old assayer's office, where miners brought their gold to be weighed. The scales are still on the counter, covered in dust. A ledger shows he paid miners a fraction of what their gold was worth. A note says 'Shot the assayer. -Pete'.",
        "An old powder magazine, built to store explosives. It's empty now, but the smell of dynamite lingers. The walls are blackened from a past explosion. One stray spark could have leveled this entire area.",
        "A set of rusted mining cart tracks leads from a mine entrance and ends abruptly at a cliff edge. An overturned cart lies at the bottom of the ravine. Someone left in a very big hurry.",
        "The foreman's cabin is surprisingly intact. A ledger is open on the desk. 'Week 52: $0 profit'. 'Week 53: 3 men dead in cave-in'. 'Week 54: Blackwood demands his cut. There is nothing left to give.'",

        # === ROW 5 (Y=5): THE OUTLAW HIDEOUTS ===
        "You've found a hidden canyon camp. The ashes from dozens of campfires are cold. Stolen goods are scattered everywhere - saddles, guns, strongboxes. The outlaws were here recently. Very recently.",
        "A cave entrance is hidden behind a waterfall. Inside, there's makeshift furniture and fresh food supplies. A bedroll is still warm. You are not alone in this cave.",
        "A frayed rope ladder disappears into a black pit in the earth. You can hear voices echoing from below. Is it laughter? Or screaming? It sounds like both. The ladder sways ominously.",
        "This small cave is a cache of stolen goods. Fine saddles, engraved revolvers, and locked strongboxes are piled high. Many of them bear the insignia of the local Sheriff's department. Interesting.",
        "A lookout post has been carved into the highest rock in the area. It provides a perfect view of the surrounding plains. An empty whiskey bottle and a spyglass are left behind. Through the glass, you see a dust cloud approaching.",
        "You find the entrance to a smuggler's tunnel, hidden beneath a false boulder. Torch brackets line the walls. Maps are scratched into the dirt floor, showing routes that bypass Blackwood's checkpoints.",
        "What looks like a solid rock wall has a faint crack. You push, and a section of the wall pivots inward, revealing a hidden passage. This is how they move without being seen.",
        "A rickety rope bridge spans a 200-foot deep gorge. Several planks are missing, and the ropes are frayed. The wind makes it swing wildly. The only way forward is one step at a time. Don't look down.",
        "A natural fortress of boulders provides a perfect defensive position. The gaps between rocks have been filled in with smaller stones, creating shooting positions. Spent shell casings litter the ground. A major battle was fought here.",
        "The embers of a campfire are still glowing. A pot of coffee is still warm over the coals. The outlaws were here just minutes ago. They will be back soon.",

        # === ROW 6 (Y=6): THE DEAD RAILROAD ===
        "You arrive at the Silver Creek Depot. A sign reads 'CLOSED'. The last train left two years ago. Tumbleweeds are tangled in the rails. The schedule board has a single word on it: 'CANCELLED'.",
        "A massive railroad water tower, built to service steam engines, looms over you. Its metal is rusted, and the ladder is broken. The tank is riddled with bullet holes. Was it target practice, or something more sinister?",
        "A derailed boxcar lies on its side like a beached whale. The doors have been blown open with dynamite. It's empty now, but the floor is littered with fragments of what were once valuable goods. A robbery gone wrong.",
        "A section of the railroad track has been deliberately sabotaged. The rails are bent and torn from the ties. The saboteurs used tools and explosives. They wanted this train to crash.",
        "A line of telegraph poles marches into the distance, but the wires have been cut. They were severed cleanly. This town has been deliberately isolated from the outside world. No messages get in or out.",
        "Inside the stationmaster's office, the telegraph machine sits silent. The last message is still on the paper tape: 'BLACKWOOD'S MEN ARE HERE. THEY'RE KILLING EVERYONE. SEND HEL--'. The message was never finished.",
        "A signal tower stands beside the tracks, its levers frozen with rust. The red and green signal lights are shattered. No one is directing the trains anymore. There are no trains to direct.",
        "The freight platform is littered with smashed crates. Most were marked 'FRAGILE' or 'MEDICAL SUPPLIES'. The manifests show a large shipment of silver was also on board. It is nowhere to be seen.",
        "A passenger car, burned to a blackened husk, sits on a siding. The seats are charred skeletons of metal. There are bullet holes in the walls. They didn't just rob the train; they burned the evidence, and the witnesses.",
        "You stand in the main rail yard, where five tracks converge. A complex switching station lies in ruins, deliberately destroyed. Several trains are rusting on the sidings, silent metal ghosts.",

        # === ROW 7 (Y=7): THE RANCHLANDS OF THE LOST ===
        "The skeleton of a cow lies picked clean by vultures. The brand 'Double-R' is still visible on its hide. There's a bullet hole in its skull. Rustlers shot it, but couldn't move it.",
        "A small line shack, a temporary home for cowboys working the range. Inside there's a single bunk, a small stove, and old supplies. A journal entry reads: 'Saw strange riders today. Not from any ranch I know.'",
        "A barbed wire fence stretches from horizon to horizon, a line drawn in the dirt. The gate hangs open, its lock cut with bolt cutters. A sign reading 'TRESPASSERS WILL BE SHOT' has been used for target practice.",
        "A windmill creaks a mournful song in the wind, pumping water into a trough. The water is clean and cool. Cattle tracks are everywhere, but they are all old. No herd has been here for months.",
        "A branding post is hung with irons from seven different ranches. All of them have been crossed out. A new, eighth brand has been seared into the wood: a skull with a star. Blackwood's mark.",
        "A massive corral, built to hold a hundred head of cattle, stands empty. The wooden posts are weathered gray by the sun. The herd was stolen, sold, or slaughtered. The ranch is dead.",
        "The cowboys' bunkhouse has bunks for a dozen men. They are all empty. Personal belongings - a harmonica, a worn bible, a letter from home - were all left behind. They fled in a hurry, or were taken in the night.",
        "The main ranch house was grand once, with a wide porch and glass windows. Now it is a decaying ruin. The front door is kicked in. Inside, family photos are trampled on the floor. 'THE ROCKING-R RANCH' sign has been burned.",
        "The roof of the main barn has partially collapsed. Hay is rotting inside, and tools are rusted. The horse stalls are empty. You hear something moving in the hayloft above. It is not a horse.",
        "In the foreman's cabin, the account books tell a story of ruin. 'Year 1: Profit $5000'. 'Year 2: Profit $2000'. 'Year 3: $0. Blackwood took the herd, the gold, and the hope.'",

        # === ROW 8 (Y=8): THE APPROACH TO BLACKWOOD'S DOMAIN ===
        "You reach a checkpoint. A crude barricade of wagons and barrels blocks the road. It's unmanned. The guards have fled, leaving their weapons behind. They feared what was behind them more than what was in front.",
        "The trees here are a macabre art gallery. Hundreds of wanted posters are nailed to them. You see your own face on the newest one, crudely drawn. '$500 DEAD OR ALIVE' is written below. Blackwood wants you badly.",
        "You come to an old oak tree. Seven ropes dangle from a thick branch, each tied in a hangman's noose. Seven names are carved into the trunk. A fresh carving at the bottom reads 'RESERVED'.",
        "A U.S. Marshal's wagon, built like a mobile prison, sits abandoned. The iron-barred door is padlocked. From inside, you hear a faint scratching and a whisper: 'He's a monster... kill him...'",
        "You stumble upon a bounty hunter camp. These are professional killers, drawn by Blackwood's gold. Trophy scalps hang from a line. A collection of wanted posters shows their targets. Yours is on top of the pile.",
        "A brand new gallows is under construction, the scent of fresh-cut pine in the air. A sign hangs from it: 'RESERVED FOR THE NEXT FOOL'. They are expecting you.",
        "A large tent serves as a makeshift courtroom. A sign reads 'CIRCUIT MAGISTRATE'. Inside, a stack of pre-written verdicts all say the same thing: 'GUILTY. SENTENCE: DEATH.' This is not a court of law; it is a butcher shop.",
        "Cells have been carved directly into the cliff face, with iron bars serving as doors. The prisoners inside are gaunt and broken. They whisper warnings through the bars: 'Turn back while you still can. No one beats Blackwood.'",
        "A guard tower provides a perfect view of all approaches to the fortress. It's empty. A high-powered sniper rifle is left behind, propped against the wall, scope trained on the path you just walked.",
        "The armory is a small, stone building with a heavy iron door and gun slits for windows. It's locked tight. Inside, there are enough guns and ammunition to wage a small war. This is the source of Blackwood's power.",

        # === ROW 9 (Y=9): SHERIFF BLACKWOOD'S FORTRESS ===
        "You have reached the outer wall of Blackwood's fortress. It is a 20-foot high wall of stone and timber, with watchtowers at the corners. This isn't a town; it's a castle built on fear.",
        "The main gate is a massive, iron-reinforced door. A human skull is mounted above it. Carved into the wood below the skull are the words 'ABANDON ALL HOPE, YE WHO ENTER HERE'. This is the point of no return.",
        "The training yard is a field of mud and blood. Shooting targets are riddled with holes. Practice dummies have been stabbed and dismembered. It becomes clear they don't just train on dummies; they train on prisoners.",
        "The barracks for Blackwood's deputies. There are fifty bunks, but most are empty. His men are deserting him. Even killers have a line they won't cross, and Blackwood crossed it long ago.",
        "The mess hall. Long tables are set for a meal, but the food is cold and untouched. A sense of dread hangs in the air. No one is eating. Everyone is preparing for the final battle.",
        "You enter Blackwood's private chapel. The Bible on the altar has had pages torn out and rewritten. A new commandment is scrawled in blood: 'I AM THE LAW AND THE LIGHT'. This is a sanctuary of madness.",
        "The war room. Maps of the entire territory cover the walls. Red pins mark towns and ranches that have been 'pacified'. Black pins mark targets that remain. There is a single black pin over your current location.",
        "The entrance to the dungeon is a stone staircase leading down into darkness. The screams of the tortured echo up from below. This is where Blackwood interrogates his enemies. This is where his power is forged.",
        "The powder room. Crates of dynamite, barrels of black powder, and boxes of ammunition are stacked floor to ceiling. This entire fortress is a bomb waiting to explode. One stray spark, and it all goes up in flames.",
        "You kick open the door to the Sheriff's office. Blackwood sits behind a massive desk made of dark, polished wood. He doesn't look surprised. 'I've been expecting you,' he growls, his hand resting on his revolver. This is the end of the line.",
    ]


def make_board(rows: int, columns: int) -> dict:
    """
    Create a game board dictionary with  room descriptions.

    :param rows: number of rows in the board
    :param columns: number of columns in the board
    :precondition: rows must be a positive integer
    :precondition: columns must be a positive integer
    :postcondition: creates a dictionary mapping coordinates to room information
    :return: dictionary with (row, column) tuple keys and room info dict values

    >>> test_board = make_board(2, 2)
    >>> (0, 0) in test_board
    True
    >>> len(test_board)
    4
    """
    coordinates = generate_coordinates(rows, columns)
    descriptions = generate_unique_room_descriptions()

    board = {}
    for index, (row, column) in enumerate(coordinates):
        if index < len(descriptions):
            description = descriptions[index]
        else:
            description = f"Location ({row}, {column}) - Unexplored territory."

        board[(row, column)] = {
            "description": description,
            "row": row,
            "column": column
        }

    return board


def get_location_description(board: dict, x_coord: int, y_coord: int) -> str:
    """
    Get the description of a location on the board.

    :param board: a dictionary representing the game board
    :param x_coord: the x-coordinate (column) of the location
    :param y_coord: the y-coordinate (row) of the location
    :precondition: board must be a valid board dictionary
    :precondition: x_coord must be an integer
    :precondition: y_coord must be an integer
    :postcondition: returns the description string for the given coordinates
    :return: string description of the location

    >>> test_board = make_board(3, 3)
    >>> description = get_location_description(test_board, 0, 0)
    >>> len(description) > 0
    True
    """
    location = board.get((y_coord, x_coord))
    if location:
        return location["description"]
    else:
        return "You see nothing but an endless void."


def display_map(rows: int, columns: int, character_x: int, character_y: int):
    """
    Display a beautiful ASCII art map of the world showing the player's position.

    :param rows: the number of rows in the map
    :param columns: the number of columns in the map
    :param character_x: the player's current X coordinate
    :param character_y: the player's current Y coordinate
    :precondition: rows, columns, character_x, character_y must be integers
    :postcondition: prints an ASCII map to the console
    :return: None

    >>> display_map(5, 5, 2, 3)
    <BLANKLINE>
      outlaw's redemption map
    ➖➖➖➖➖➖➖➖➖➖➖➖
    | . . . . . | N ↑       |
    | . . . . . |           |
    | . . . . . | W ←   → E |
    | . . 🏃‍. . |           |
    | . . . . . | S ↓       |
    ➖➖➖➖➖➖➖➖➖➖➖➖
    KEY: [🏃‍] You are here
    <BLANKLINE>
    """
    print("\n Outlaw's Redemption Map")
    print("➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖")
    for r in range(rows):
        map_row = "| "
        for c in range(columns):
            if r == character_y and c == character_x:
                map_row += "🏃‍♂️ "
            else:
                map_row += "⚪️ "
        if r == 0:
            map_row += "| N ↑       |"
        elif r == 2:
            map_row += "|           |"
        elif r == 3:
            map_row += "| W ←   → E |"
        elif r == 5:
            map_row += "|           |"
        elif r == 6:
            map_row += "| S ↓       |"
        else:
            map_row += "|           |"

        print(map_row)
    print("➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖")
    print("KEY: [🏃‍♂️] You are here")
    print()


if __name__ == "__main__":
    display_map(10, 10, 3, 4)