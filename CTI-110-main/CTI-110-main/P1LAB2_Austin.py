# CTI 110
# P1LAB2 - Selling Things
# Austin Lee
# 9/3/2026

# Fictional Store -- pick three things
# product_name, product_count, product_price

# change these to your own values
product_name = "brownie" # strings use "quotes" and are made of text
product_count = 100       # integers are whole numbers, no decimal
product_price = 2.00    # doubles are decimal numbers

# Instead. we ask the user with input()
print("STORE STARTUP")
print("_" * 10) # ten _ in a row
product_name = input("Enter product name: ")
product_count = input("Enter product count: ")
product_price = input("Enter unit price: ")

# PROCESSING
product_count = int(product_count)  # convert string to integer: "100" -> 100
product_price = float(product_price)# convert string to float: "3.25" -> 3.25
total = product_count * product_price # requires two numbers, returns a third number


# OUTPUT
print("CUSTOMER INTERFACE")
print("_" * 10) # ten _ in a row
print("welcome to the", product_name, "store")
print(f"we have {product_count} {product_name}(s) at ${product_price:.2f} each.")
print(f"total is: ${total:.2f}.")


