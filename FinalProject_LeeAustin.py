# Austin Lee
# 11/10/2026
# Final Project
# Making a game for the final project

# treasure chest opening game with different characters to choose from that can impact your performance within the game.

import random

# CHARACTER DATA
characters = {
    "1": {
        "name": "Knight",
        "luck": 10,
        "strength": 90,
        "magic": 20
    },
    "2": {
        "name": "Rogue",
        "luck": 80,
        "strength": 40,
        "magic": 30
    },
    "3": {
        "name": "Wizard",
        "luck": 60,
        "strength": 20,
        "magic": 90
    },
    "4": {
        "name": "Ranger",
        "luck": 65,
        "strength": 65,
        "magic": 40
    }
}

# TREASURE CHESTS
treasures = [
    ("Wooden Chest", 50, 70),
    ("Silver Chest", 100, 150),
    ("Golden Chest", 200, 300),
    ("Legendary Chest", 500, 1000)
]

# CHARACTER SELECTION
print("================================")
print("     TREASURE CHEST QUEST")
print("================================")

print("\nChoose your character:")

for key, character in characters.items():
    print(f"{key}. {character['name']}")

choice = input("\nEnter your choice (1-4): ")

while choice not in characters:
    print("Invalid choice!")
    choice = input("Choose a character (1-4): ")

player = characters[choice]

print(f"\nYou selected {player['name']}!")

# DISPLAY CHARACTER STATS
print("\nYour Stats:")
print("Luck:", player["luck"])
print("Strength:", player["strength"])
print("Magic:", player["magic"])

# GAME VARIABLES
gold = 0
chests_opened = 0

# GAME LOOP
while chests_opened < 5:

    print("\n==============================")
    print("A treasure chest appears!")
    print("==============================")

    print("1. Open the chest")
    print("2. Skip the chest")
    print("3. View your stats")
    print("4. Quit game")

    action = input("\nWhat would you like to do? ")

    if action == "1":

        # Select random chest
        chest = random.choice(treasures)

        chest_name = chest[0]
        min_gold = chest[1]
        max_gold = chest[2]

        print(f"\nYou found a {chest_name}!")

        # Character performance bonus
        bonus = player["luck"] / 100

        if player["name"] == "Knight":
            bonus += player["strength"] / 500

        elif player["name"] == "Wizard":
            bonus += player["magic"] / 500

        elif player["name"] == "Rogue":
            bonus += player["luck"] / 200

        elif player["name"] == "Ranger":
            bonus += player["strength"] / 500

        # Calculate treasure reward
        reward = random.randint(min_gold, max_gold)

        reward = int(reward * (1 + bonus))

        gold += reward
        chests_opened += 1

        print("\nCongratulations!")
        print(f"You earned {reward} gold!")

    elif action == "2":
        print("You skipped the chest.")

    elif action == "3":
        print("\nPLAYER STATS")
        print("Character:", player["name"])
        print("Gold:", gold)
        print("Chests opened:", chests_opened)

    elif action == "4":
        print("\nThanks for playing!")
        break

    else:
        print("Invalid option!")
        continue

    if chests_opened == 5:
        print("\nYou opened all 5 treasure chests!")

# FINAL SCORE
print("\n==============================")
print("         GAME OVER")
print("==============================")
print("Character:", player["name"])
print("Total Gold:", gold)
print("Chests Opened:", chests_opened)
print("==============================")
