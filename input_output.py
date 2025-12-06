"""
input_output.py
Demonstrates how to take input from the user and display output in Python.
"""

# Taking a simple string input
name = input("Enter your name: ")
print(f"Hello, {name}!")


# Taking numeric input and converting types
age_input = input("Enter your age: ")

# input() always returns a string, so we convert it to int
age = int(age_input)
print(f"Next year you will be {age + 1} years old.")


# Taking multiple inputs for a small calculation
price_input = input("Enter the price of the product: ")
quantity_input = input("Enter the quantity: ")

price = float(price_input)
quantity = int(quantity_input)
total_cost = price * quantity

print(f"Total cost: {total_cost}")


# Using input with conditions
choice = input("Do you like Python? (yes/no): ").strip().lower()

if choice == "yes":
    print("Nice! Keep learning and building.")
elif choice == "no":
    print("Give it some time, it will grow on you.")
else:
    print("Interesting answer! Keep exploring.")
