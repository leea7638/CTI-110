# CTI 110
# P4LAB2
# Austin Lee
# 10/08/2026

# counting loop
print ("7's times tables:")
for multi in range(1, 13):
    print (7 * multi)

# set up variables
# start the main loop
again = "yes" 
while again == "yes":
    # Ask the user for their chosen integer (0-12)
    multiplier = int(input("Enter a number 1-12: "))
    # validate (loop) - number must be between 0 and 12
    while multiplier < 0 or multiplier > 12:
        print("that is not a valid number.")
        multiplier = int(input("Enter a number 1-12: "))

    # print the times table header
    print("Multiplication Table")
    print("-"*20)
    # print the times table (loop)
    for number in range(1, 13):
        print(multiplier, "*", number, "=", number*multiplier)
    # Finally, ask if they want to repeat
    again = input("Run again? (yes/no) ")
    


