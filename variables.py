"""
variables.py
Demonstrates different types of variables in Python with clear examples.
"""

# String
name = "Subham Bhattacharya"

# Integer
age = 22

# Float
height_cm = 173.5

# Boolean
is_learning_python = True

# List (mutable collection)
skills = [
    "Python",
    "HTML",
    "Git",
    "AI Basics",
    "Prompt Engineering",
    "Automation with Python",
    "Problem Solving"
]

# Dictionary (key-value data)
profile = {
    "name": name,
    "age": age,
    "skills": skills,
    "active_learner": is_learning_python
}

# Printing values in a clean way
print("----- User Profile -----")
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Height: {height_cm} cm")
print(f"Learning Python: {is_learning_python}")
print(f"Skills: {skills}")

print("\nFull Profile Dictionary:")
print(profile)
