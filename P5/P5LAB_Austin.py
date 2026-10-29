# CTI 110
# P5LAB - Purchase and change
# Austin Lee
# 10/29/26
# Self checkout machine simulator. makes change.

import random

# put other functions here.
def disperse_change(amount):
    # Print out the change needed.
    # Input: float
    # return: nothing
    print(f"change is: ${amount:.2f}")
    print()
    cents = round(amount * 100) # Convert to cents, round correctly
    print("That's", cents,"cents.")

    # For each currency type:
    # - cents // [CURRENCY] gives you how many CURRENCY
    # - cents % [CURRENCY] gives you the left over cents.
    dollars = cents // 100
    cents   = cents % 100
    # if statement - dont show of zero, use singular or plural otherwise
    if dollars == 1:
        print("1 dollar")
    if dollars > 1:
        print(dollars, "dollars")

    # quarters
    quarters = cents // 25
    cents    = cents % 25
    if quarters == 1:
        print("1 quarter")
    if quarters > 1:
        print(quarters, "quarters")

    # Dimes
    dimes = cents // 10
    cents = cents % 10
    if dimes == 1:
        print("1 dime")
    if dimes > 1:
        print(dimes, "dimes")

    # nickels
    nickels = cents // 5
    cents   = cents % 5
    if nickels == 1:
        print("1 nickel")
    if nickels > 1:
        print(nickels, "nickels")

    # pennies
    pennies = cents // 1
    cents   = cents % 1
    if pennies == 1:
        print("1 penny")
    if pennies > 1:
        print(pennies, "pennies")

    

# Main
def main():
    # Declare variables
    cost = 0.0
    amount_paid = 0.0
    change_owed = 0.0 
    print("Welcome to the self-checkout sim")
    # Generate a random float value for the cost - uniform picks a number in this range
    cost = round(random.uniform(0.01, 100.00), 2)
    print(f"you owe: ${cost:.2f}")
    # Ask the user how much $ they put in
    amount_paid = float(input("How much money do you put in the self checkout? $"))
    # Calc change owed
    change_owed = amount_paid - cost

    print("Here is your change: ")
    disperse_change(change_owed)





# last line - start the program
main()