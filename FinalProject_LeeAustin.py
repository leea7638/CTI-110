# Austin Lee
# 11/10/2026
# Final Project
# Making a game for the final project

# treasure chest opening game with different characters to choose from that can impact your performance within the game.

import random

# CHARACTER DATA
characters = {
    "1": {
        "name": "Enforcer",
        "luck": 10,
        "strength": 90,
        "magic": 20
    },
    "2": {
        "name": "Robber",
        "luck": 80,
        "strength": 40,
        "magic": 30
    },
    "3": {
        "name": "Chemist",
        "luck": 60,
        "strength": 20,
        "magic": 90
    },
    "4": {
        "name": "Freelancer",
        "luck": 65,
        "strength": 65,
        "magic": 40
    }
}

# TREASURE CHESTS
treasures = [
    ("Lockbox", 50, 100),
    ("Strongbox", 300, 550),
    ("Security Safe", 700, 1000),
    ("Bank Vault", 5000, 10000)
]

# CHARACTER SELECTION
print("================================")
print("     Safe Escape")
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
cash = 0
safes_opened = 0

# GAME LOOP
while safes_opened < 5:

    print("\n==============================")
    print("you find a Random Safe")
    print("==============================")

    print("1. Open the safe")
    print("2. Skip the safe")
    print("3. View your stats")
    print("4. Quit game")

    action = input("\nWhat would you like to do? ")

    if action == "1":

        # Select random chest
        safe = random.choice(cash)

        safe_name = safe[0]
        min_cash = safe[1]
        max_cash = safe[2]

        print(f"\nYou found a {safe_name}!")

        # Character performance bonus
        bonus = player["luck"] / 100

        if player["name"] == "Enforcer":
            bonus += player["strength"] / 500

        elif player["name"] == "Chemist":
            bonus += player["magic"] / 500

        elif player["name"] == "Raider":
            bonus += player["luck"] / 200

        elif player["name"] == "Freelancer":
            bonus += player["strength"] / 500

        # Calculate treasure reward
        reward = random.randint(min_cash, max_cash)

        reward = int(reward * (1 + bonus))

        cash += reward
        safes_opened += 1

        print("\nCongratulations!")
        print(f"You earned {reward} dollars!")

    elif action == "2":
        print("You skipped the safe.")

    elif action == "3":
        print("\nPLAYER STATS")
        print("Character:", player["name"])
        print("Cash:", cash)
        print("Safes opened:", safes_opened)

    elif action == "4":
        print("\nThanks for playing!")
        break

    else:
        print("Invalid option!")
        continue

    if safes_opened == 5:
        print("\nYou opened all 5 safes!")

def open_chest(character):

    print(f"\n{character} approaches the safe...")

    if character == "Robber":
        print("You disarm the security alarm.")
        print("You safely collect the cash.")

    elif character == "Chemist":
        print("You geiger counter detects fissle material.")
        print("the alarm activates, releasing a poisoness gas.")
        print("you are protected from the gas with your chem suit.")

    elif character == "Enforcer":
        print("You force the safe open!")
        print("The alarm activates and gunshot goes off.")
        print("you got hit but your body armor protects you.")

    else:
        print("You open the safe...")
        print("the alarm goes off and a gunshot goes off.")
        print("Your health is now 25% wer.")

# FINAL SCORE
print("\n==============================")
print("         GAME OVER")
print("==============================")
print("Character:", player["name"])
print("Total Cash:", cash)
print("Safes Opened:", safes_opened)
print("==============================")
