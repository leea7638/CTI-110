# CTI 110
# P1HW1 - Math
# Austin Lee
# 9/8/2026
# do some math processing

# PART 1 - Exponents

# PART 2 - ADDITION SUBTRACTION
# 3 numbers, start, add_this, sub_this
start = int(input("Enter the starting integer"))
#print("you typed", start)
add_this = int(input("Enter integer to add: "))
sub_this = int(input("Enter integer to subtract "))
# calculate the answer
answer = start + add_this - sub_this
# print the answer
print()
print() # that gives 2 newlines, so would print("/n")
# should look like: "10 + 4 - 2 is equal to 12"
print(start, "+", add_this, "-", sub_this, "is equal to", answer)
print(f"{start} + {add_this} - {sub_this} is equal to {answer}")

