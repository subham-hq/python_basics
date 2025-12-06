"""
functions.py
Demonstrates how to define and use functions in Python
with simple, practical examples.
"""

# Basic function with no parameters
def say_hello():
    print("Hello from a function!")


# Function with one parameter
def greet(name):
    return f"Hello, {name}!"


# Function with multiple parameters
def add_numbers(a, b):
    return a + b


# Function with a default parameter
def introduce(name, country="India"):
    return f"My name is {name} and I am from {country}."


# Function that uses a list
def count_skills(skills):
    return len(skills)


# Function with a simple decision (if/else)
def is_adult(age):
    if age >= 18:
        return True
    return False


# Calling the functions and printing results
if __name__ == "__main__":
    say_hello()

    message = greet("Subham")
    print(message)

    result = add_numbers(10, 5)
    print(f"10 + 5 = {result}")

    intro = introduce("Subham")
    print(intro)

    skills = ["Python", "HTML", "Git", "AI Basics", "Automation with Python"]
    print(f"Number of skills: {count_skills(skills)}")

    age = 24
    print(f"Is {age} an adult? {is_adult(age)}")
