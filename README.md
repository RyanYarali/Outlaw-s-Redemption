# 🤠 OUTLAW'S REDEMPTION 🔥

> *"The law has become the outlaw.  Will you bring justice, or become what you seek to destroy?"*

A terminal-based Western RPG where your choices matter. Built with Python, powered by ANSI colors, and driven by revenge. 

**By Ryan Yarali** | Student ID: A01464263 | [@RyanYarali](https://github.com/RyanYarali)

---

## 🎬 THE STORY

**1885.  Dusty Gulch, Arizona Territory.**

Sheriff Blackwood rules with an iron fist. His corruption runs deeper than the mines, his cruelty colder than the desert nights.  Innocent blood stains the gallows.  The law has become the outlaw. 

You ride into town—a wanderer with a dark past and nothing to lose. The townsfolk whisper your name with hope.  Or fear. 

**Your choices will write your legend.**

Will you be the hero this dying town desperately needs?  Or will you take what you can and disappear into the sunset, leaving only dust and broken promises?

The frontier doesn't forgive. But it never forgets.

---

## 🎮 GAMEPLAY SHOWCASE

```
╔══════════════════════════════════════════════════════════════════════════╗
║                                                                          ║
║ ░█▀█░█░█░▀█▀░█░░░█▀█░█░█░▀░█▀▀░░░█▀▄░█▀▀░█▀▄░█▀▀░█▄█░█▀█░▀█▀░▀█▀░█▀█░█▀█ ║
║ ░█░█░█░█░░█░░█░░░█▀█░█▄█░░░▀▀█░░░█▀▄░█▀▀░█░█░█▀▀░█░█░█▀▀░░█░░░█░░█░█░█░█ ║
║ ░▀▀▀░▀▀▀░░▀░░▀▀▀░▀░▀░▀░▀░░░▀▀▀░░░▀░▀░▀▀▀░▀▀░░▀▀▀░▀░▀░▀░░░░▀░░▀▀▀░▀▀▀░▀░▀ ║
║                                                                          ║
╚══════════════════════════════════════════════════════════════════════════╝

You stand at the edge of a dusty canyon.  The wind howls. 
A tumbleweed rolls past.  Your hand rests on your revolver. 

Location: (3, 5) | HP: 150/150 | Gold: 250 | Level: 2 | Honor: 25

Your move?  [N/S/E/W, M, I, $, Q]
>>> 
```

---

## ⚡ QUICK START

**Get playing in 30 seconds:**

```bash
# Clone it
git clone https://github.com/RyanYarali/COMP-1510-202530-TERM-PROJECT.git

# Run it
cd COMP-1510-202530-TERM-PROJECT
python main.py

# Enjoy it 🤠
```
(Or use your IDE terminal)

**Requirements:** Python 3.6+ | Terminal with ANSI color support

---

## 🎯 HOW TO WIN

Complete all three objectives to claim victory:

### 1️⃣ GAIN EXPERIENCE
- Fight bandits, outlaws, and corrupt lawmen
- Make moral choices (do you help or hurt?)
- Solve riddles from mysterious strangers
- **Target:** Reach Level 3 (250 XP total)

### 2️⃣ REACH THE FORTRESS
- Navigate the 10×10 frontier map
- Avoid getting lost in the canyons
- **Target:** Arrive at coordinates (9, 9)

### 3️⃣ DEFEAT SHERIFF BLACKWOOD
- Face the final boss in an epic showdown
- Survive his deadly revolver attacks
- **Target:** Reduce his 200 HP to zero

---

## 🎮 CONTROLS

| Key | Action |
|-----|--------|
| **N** | Move North ⬆️ |
| **S** | Move South ⬇️ |
| **E** | Move East ➡️ |
| **W** | Move West ⬅️ |
| **M** | Display Map 🗺️ |
| **I** | Character Info 📊 |
| **$** | Visit Shop 🏪 |
| **Q** | Quit Game 🚪 |

---

## 🔥 CORE FEATURES

### ⚔️ COMBAT SYSTEM
Turn-based gunfights with scaling difficulty:
- Dynamic enemy generation based on your level
- Tactical decision-making (fight or flee...  wait, you can't flee)
- Earn XP and Gold for every victory
- **Die once, game over**


### ⚖️ HONOR SYSTEM
**Your choices define you.**

Face 10 unique moral dilemmas:
- **Help** an old woman → +Honor, +XP, -Gold
- **Rob** a stagecoach → -Honor, -XP, +Gold
- **Ignore** the problem → Neutral

**Your ending depends on your Honor:**
- **Honor ≥ 50:** 🏆 Hero's Legacy (donate all gold, rebuild town)
- **Honor < 50:** 💰 Feared Name (keep gold, leave alone)

### 🧩 RIDDLE ENCOUNTERS
Mysterious strangers test your wit:
- 10 unique riddles
- **Correct:** +35 XP, +50 Gold
- **Wrong:** +10 XP (pity prize)

*Example:*
```
A hooded figure blocks your path... 

"I speak without a mouth and hear without ears. 
I have no body, but I come alive with wind. 
What am I?"

>>> echo
```

### 💰 THE GENERAL STORE
**Spend gold to survive.**

| Item | Effect | Cost |
|------|--------|------|
| Small Health Potion | +50 HP | 30 Gold |
| Large Health Potion | +100 HP | 50 Gold |
| **Full Restoration** | Full HP | 80 Gold |
| Experience Boost | +25 XP | 50 Gold |
| **Lucky Charm** | +50 XP | 100 Gold |

**🔥 PRO TIP:** You can shop **DURING THE BOSS FIGHT! **

### 👹 FINAL BOSS: SHERIFF BLACKWOOD

When you reach (9,9) at Level 3, the showdown begins:

```
              S H E R I F F   B L A C K W O O D
                              ___
                            _/   \_
                           / \___/ \
                          /  |   |  \
                         |   O   O   |
                         |    \_/    |
                          \  \_____/  /
                           \___|||___/
                               |||
                          ___/  |  \___
                         |      |      |
                         |   ★  |  ★   |

"The law has come for you, outlaw.  Time to hang."
```

**Boss Stats:**
- HP: 350
- Damage: 30-45 per round
- **You can visit shop mid-fight!**

---

## 🗺️ THE FRONTIER

Explore 100 unique locations across a 10×10 grid:

**Sample Locations:**
- *"An abandoned saloon.  Whiskey bottles litter the floor."*
- *"A dried-up creek bed. Death Valley feels close."*
- *"The gallows. Three ropes sway in the wind."*
- *"A canyon overlook. You can see for miles."*

---

## 🔓 SECRET CHEAT CODES

**For testing, speedrunning, or pure chaos.**

Just type these instead of a command:

| Code | Effect |
|------|--------|
| `HEAL` | Instant full HP restore |
| `GOLD` | +500 gold |
| `LEVELUP` | Become Level 3 instantly |
| `BOSS` | Teleport to (9,9) |
| `GOD` | **GOD MODE** (HP: 999, Gold: 9999, Level: 3) |

**Example:**
```
Your move? [N/S/E/W, M, I, $, Q]
>>> GOD

🔥🔥🔥 ULTIMATE CHEAT ACTIVATED!  🔥🔥🔥
HP: 999 | Gold: 9999 | Level: 3 | Honor: 100
```

---

## 🧪 TESTING SUITE

**Professional-grade testing with 100% function coverage.**

### Test Statistics
- **26 test files** (one per function)
- **81+ individual test cases**
- **3+ tests per function minimum**
- **Zero tolerance for untested code**


### Test Structure
```
tests/
├── test_make_board.py               
├── test_get_location_description.py 
├── test_make_character.py           
├── test_is_alive.py                 
├── test_character_has_leveled. py    
├── test_level_up_character.py       
├── test_validate_move.py            
├── test_move_character.py           
├── test_make_enemy.py               
├── test_combat. py                   
├── test_check_for_challenges.py     
├── test_determine_encounter_type.py 
├── test_execute_challenge_protocol.py 
├── test_handle_honor_choice.py      
├── test_handle_riddle. py            
├── test_display_shop. py             
├── test_shop_menu.py                
├── test_check_cheat_code.py         
├── test_show_cheat_menu.py          
├── test_execute_boss_fight.py       
├── test_display_victory_ending.py   
├── test_display_game_over.py        
├── test_get_player_name.py          
├── test_game_loop.py                
├── test_display_map.py              
├── test_display_character_stats.py  
└── test_get_user_choice.py
```

---


### File Structure
```
│
├── main.py              # Entry point (runs game_loop)
├── game.py              # Main loop, boss fight, endings
├── board.py             # 100 locations, map display
├── character.py         # Stats, leveling, creation
├── utils.py             # Movement, input validation
├── combat.py            # Enemy generation, combat logic
├── encounters.py        # Riddles, choices, encounter system
├── shop.py              # Shop menu, item purchases
├── cheats.py            # Cheat code system
├── color. py             # ANSI color constants
├── README.md            # This file
│
└── 🧪 tests/               # Complete test suite
    ├── test_make_board.py
    ├── test_get_location_description.py
    ├── test_make_character.py
    ├── test_is_alive.py
    ├── test_character_has_leveled.py
    ├── test_level_up_character.py
    ├── test_validate_move. py
    ├── test_move_character.py
    ├── test_make_enemy. py
    ├── test_combat.py
    ├── test_check_for_challenges. py
    ├── test_determine_encounter_type.py
    ├── test_execute_challenge_protocol.py
    ├── test_handle_honor_choice.py
    ├── test_handle_riddle.py
    ├── test_display_shop.py
    ├── test_shop_menu.py
    ├── test_check_cheat_code.py
    ├── test_show_cheat_menu.py
    ├── test_execute_boss_fight.py
    ├── test_display_victory_ending.py
    ├── test_display_game_over.py
    ├── test_get_player_name.py
    ├── test_game_loop.py
    ├── test_display_map.py
    ├── test_display_character_stats.py
    └── test_get_user_choice.py
```

---

## 📊 GAME STATISTICS

### Progression System
- **Levels:** 3 total
- **Level 1 → 2:** 100 XP required
- **Level 2 → 3:** 250 XP total required
- **HP Gain:** +50 HP per level
- **Starting Stats:** 100 HP, 100 Gold, Level 1

### Content Volume
- **Locations:** 100 unique descriptions
- **Encounters:** (combats, 10 choices, 10 riddles)
- **Shop Items:** 5 purchasable items
- **Endings:** 2 (based on Honor)
- **Cheat Codes:** 5 functional codes

### Technical Metrics
- **Lines of Code:** ~2000+
- **Functions:** 26 across 10 modules
- **Test Cases:** 81+
- **Color Codes:** 8 ANSI colors used
- **ASCII Art Pieces:** 10+

---

## 🎓 LEARNING OUTCOMES

This project demonstrates mastery of:

### Python Fundamentals
✅ Functions (26 unique functions)  
✅ Dictionaries (character, board, enemies)  
✅ Lists (locations, encounters, shop items)  
✅ Control flow (if/elif/else, while loops)  
✅ Random module (encounters, combat)  

### Software Engineering
✅ Modular design (8 separate modules)  
✅ Documentation (full docstrings with preconditions/postconditions)  
✅ Testing (unittest framework, 81+ tests)  
✅ Version control (Git/GitHub)  
✅ Code organization (clear file structure)  

### User Experience
✅ ANSI color coding (readability)  
✅ ASCII art (immersion)  
✅ Clear prompts (usability)  
✅ Input validation (error handling)  
✅ Engaging narrative (storytelling)  

---

## 🎨 VISUAL DESIGN

### Color Palette
- 🔴 **Red** → Danger, boss, damage, death
- 🟢 **Green** → Success, healing, HP, victory
- 🟡 **Yellow** → Gold, warnings, story, tips
- 🔵 **Blue** → Information, location
- 🟣 **Magenta** → Level up, XP, achievements
- 🔵 **Cyan** → Shop, prompts, commands

### ASCII Art Gallery
- Title banner (game logo)
- Sheriff Blackwood sprite (boss)
- Victory screen (hero's legacy)
- Defeat screen (game over)
- Combat animations (gunfights)
- HP bars (visual health tracking)
- Shop storefront (general store)
- Map display (grid visualization)

---

## 🚀 FUTURE ENHANCEMENTS

**Ideas for V2.0:**

- [ ] **Save/Load System** (JSON-based game state persistence)
- [ ] **Multiplayer Mode** (co-op or versus)
- [ ] **More Endings** (4-6 endings based on choices)
- [ ] **Side Quests** (optional missions for bonus rewards)
- [ ] **Inventory System** (carry items, manage resources)
- [ ] **Difficulty Settings** (Easy, Normal, Hard, Nightmare)
- [ ] **Achievement System** (unlock badges for milestones)
- [ ] **Sound Effects** (terminal beeps for combat)
- [ ] **Boss Rush Mode** (fight all bosses back-to-back)
- [ ] **Speedrun Timer** (track completion time)

---

## 🤝 CONTRIBUTING

**Want to improve the game?**

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3.  Commit changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

**Guidelines:**
- Follow existing code style
- Add tests for new functions
- Update README if adding features
- Keep commits atomic and descriptive

---

## 🙏 ACKNOWLEDGMENTS

**Inspired by:**
- Red Dead Redemption (Rockstar Games)
- The Oregon Trail (MECC)
- Classic MUDs and text adventures

**Technical Thanks:**
- ANSI escape codes documentation
- Python unittest framework
- BCIT COMP 1510 course materials

**Special Thanks:**
- Coffee ☕
- Late nights 🌙
- The frontier spirit 🤠

---

## 📄 LICENSE

**Educational Project**  
COMP 1510 - Programming Methods  
British Columbia Institute of Technology (BCIT)  
All rights reserved.

This project is for educational purposes only.  Not licensed for commercial use.

---

## 📞 CONTACT

**Ryan Yarali**  
Student ID: A01464263  
GitHub: [@RyanYarali](https://github. com/RyanYarali)  
Course: COMP 1510 - 202530  
Institution: BCIT

---

## 🎮 READY TO PLAY?

```bash
python main.py
```

**Good luck, stranger.  The frontier awaits. ** 🤠🔫

---
