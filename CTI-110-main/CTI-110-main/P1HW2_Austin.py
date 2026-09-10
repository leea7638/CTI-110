# CTI 110
# P1HW2 - Math
# Austin Lee
# 9/8/2026
# do basic math on numbers

# Ask user to enter their budget
print("This program calculates and displays travel expenses")
budget = int(input("what is your Budget? "))

# Ask user to enter travel destination
destination = input("Enter your destination: ")

# Ask user for amount they will spend on gas
Fuel = int(input("how much do you think you will spend on gas? "))

# Ask user for amount they will spend on accommodation
hotel = int(input("Approximatley, how much will you need for accomodation/hotel? "))

# Ask user for amount they will spend on food
food = int(input("Lastly, how much do you need for food? "))

# Show location and budget
print("-----------Travel Expenses-----------")
print("Location: ", destination)
print("Initial Budget: ", budget)

# Add expenses
expenses = Fuel + hotel + food
print("Fuel:", Fuel)
print("Accomodation: ", hotel)
print("Food: ", food)
print("expenses: ", expenses)

# Subtract expenses from budget
balance = budget - expenses


# Display results
print("balance: ", balance)