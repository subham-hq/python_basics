"""
conditions.py
Demonstrates the use of conditional statements in Python
with clear and practical examples.
"""

# Basic if condition
age = 22

if age >= 18:
    print("You are eligible to vote.")


# if-else condition
temperature = 25

if temperature > 30:
    print("It is a hot day.")
else:
    print("The weather is pleasant.")


# if-elif-else condition
marks = 78

if marks >= 90:
    print("Grade: A+")
elif marks >= 75:
    print("Grade: A")
elif marks >= 60:
    print("Grade: B")
else:
    print("Grade: C")


# Comparison operators example
a = 10
b = 20

print("a == b:", a == b)
print("a != b:", a != b)
print("a > b:", a > b)
print("a < b:", a < b)


# Logical operators example
is_student = True
has_id_card = False

if is_student and has_id_card:
    print("Entry allowed.")
else:
    print("Entry not allowed.")


# Nested if example
number = 15

if number > 0:
    if number % 2 == 0:
        print("The number is positive and even.")
    else:
        print("The number is positive and odd.")
else:
    print("The number is negative or zero.")
