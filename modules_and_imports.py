"""
modules_and_imports.py
Demonstrates how to use built-in modules and custom imports in Python.
"""

# Importing a built-in module
import math

number = 25
square_root = math.sqrt(number)
print(f"Square root of {number} is: {square_root}")

print(f"Value of pi: {math.pi}")


# Importing specific functions from a module
from math import pow

result = pow(2, 3)
print(f"2 raised to the power of 3 is: {result}")


# Importing a built-in random module
import random

random_number = random.randint(1, 10)
print(f"Random number between 1 and 10: {random_number}")


# Example of a custom function (simulating import usage)
def greet(name):
    return f"Hello, {name}!"


message = greet("Subham")
print(message)
