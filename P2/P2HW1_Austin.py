# CTI 110
# P2HW1
# Austin Lee
# 9/17/2026

print("This program calculates and displays travel expenses")

budget = int(input("Enter Budget: "))
destination = input("Enter Your Travel Destination: ")
gas = int(input("How much do you think you will spend on gas? "))
hotel = int(input("Approximately, how much do you think you will spend on accomodations? "))
food = int(input("Last, how much do think you will spend on food? "))

remaining_balance = budget - (gas + hotel + food)

print("-----------Travel Expenses-----------")
print(f"{"Location:":<15} {destination:<15}")
print(f"{"Initial Budget:":<15} ${budget:<15.2f}")
print(f"{"Fuel:":<15} ${gas:<15.2f}")
print(f"{"Accomodation:":<15} ${hotel:<15.2f}")
print(f"{"Food:":<15} ${food:<15.2f}")
print("-------------------------------------")

print(f"{"Remaining Balance:":<15} ${remaining_balance:<15.2f}")

