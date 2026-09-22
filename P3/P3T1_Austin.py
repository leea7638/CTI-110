# CTI 110
# P3LAB1 - Dungeon Gatekeeper
# Austin Lee
# 9/22/2026

# main() -- this is the program's starting point.
# You dont need to use it, but it's a very good idea.
def main():
    print("Hello and welcome to the dungeon.")
    level = int(input("What level are you? "))
    if level >= 21:
        print("You can enter the dragons spire dungeon.")
    else:
        print("Try leveling up first.")

    # part 2 - List your potions
    print("time to enter the dungeon.")
    potions = int(input("how many health potions did you bring? "))
    if potions == 0:
        print("its dangerous to go alone without potions.")
    elif potions == 1:
        print(f"you have {potions} health potion.")
    elif potions >= 1:
        print(f"you have {potions} health potions.")
    else:
        print(f"how did you get {potions}??? thats less than zero.")

    # part 3 - Boss battle
    print("you are facing the ☠️SKELETON KING☠️")
    print("This will be a hard fight...")
    if level >= 25:
        # your tough enough to hit him...
        if potions > 20:
            print("It takes twenty potions to get him to low health!")
            print("***YOU WIN***")
        else:
            print("you run out of healing before killing him.")
            print("***GAME OVER, LEARN TO MAKE MORE POTIONS***")
    else:
        print("Your not doing enough damage!!")
        print("***GAME OVER***")

        
# at the bottom -- start the program
main()
