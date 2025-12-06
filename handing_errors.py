"""
error_handling.py
Demonstrates how to handle errors in Python using try, except, else, and finally.
"""

# Handling invalid integer input
age_input = input("Enter your age: ")

try:
    age = int(age_input)
    print(f"You entered age: {age}")
except ValueError:
    print("Invalid input. Please enter a number for age.")


# Handling division by zero
numerator_input = input("\nEnter a number to divide: ")
denominator_input = input("Enter a number to divide by: ")

try:
    numerator = float(numerator_input)
    denominator = float(denominator_input)
    result = numerator / denominator
except ValueError:
    print("Invalid input. Please enter valid numbers.")
except ZeroDivisionError:
    print("Cannot divide by zero. Please enter a non-zero number.")
else:
    print(f"Result of division: {result}")


# Using finally (runs whether error happens or not)
print("\nFile operation example (simulated):")

file_name = "data.txt"

try:
    print(f"Trying to open file: {file_name}")
    # Simulating file open failure with an exception
    raise FileNotFoundError("File not found.")
except FileNotFoundError as error:
    print(f"Error: {error}")
finally:
    print("Finished file operation (clean-up step).")


# Custom function with error handling
def safe_convert_to_int(value):
    """
    Tries to convert the given value to an integer.
    Returns an integer if successful, otherwise returns None.
    """
    try:
        return int(value)
    except ValueError:
        print(f"Cannot convert '{value}' to an integer.")
        return None


print("\nCustom function example:")
user_value = input("Enter a value to convert to integer: ")
converted_value = safe_convert_to_int(user_value)
print(f"Converted value: {converted_value}")
