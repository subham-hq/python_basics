"""
loops.py
Demonstrates the use of for-loops and while-loops in Python
with practical and readable examples.
"""

# For loop using range
print("For loop with range:")
for i in range(1, 6):
    print(f"Iteration number: {i}")

# For loop with a list
print("\nFor loop with a list:")
skills = [
    "Python",
    "HTML",
    "Git",
    "AI Basics",
    "Prompt Engineering",
    "Automation with Python",
    "Problem Solving"
]

for skill in skills:
    print(f"Learning: {skill}")

# While loop example
print("\nWhile loop example:")
counter = 1

while counter <= 5:
    print(f"Counter value: {counter}")
    counter += 1

# Break example
print("\nBreak example:")
for num in range(1, 10):
    if num == 5:
        print("Stopping the loop at", num)
        break
    print(num)

# Continue example
print("\nContinue example:")
for num in range(1, 6):
    if num == 3:
        print("Skipping", num)
        continue
    print(num)
