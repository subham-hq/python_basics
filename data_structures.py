"""
data_structures.py
Demonstrates the core data structures in Python:
list, tuple, set, and dictionary with practical examples.
"""

# List (Ordered and Mutable)
skills = ["Python", "HTML", "Git"]
skills.append("AI Basics")

print("List Example:")
print("Skills:", skills)
print("First skill:", skills[0])
print("Total skills:", len(skills))


# Tuple (Ordered and Immutable)
coordinates = (10, 20)

print("\nTuple Example:")
print("Coordinates:", coordinates)
print("X value:", coordinates[0])
print("Y value:", coordinates[1])


# Set (Unordered and Unique Values)
unique_numbers = {1, 2, 3, 3, 4, 5, 5}

print("\nSet Example:")
print("Unique numbers:", unique_numbers)
unique_numbers.add(6)
print("After adding 6:", unique_numbers)


# Dictionary (Key-Value Pairs)
user_profile = {
    "name": "Subham",
    "age": 22,
    "skills": skills,
    "is_active": True
}

print("\nDictionary Example:")
print("User Profile:", user_profile)
print("User Name:", user_profile["name"])
print("User Skills:", user_profile["skills"])

# Updating dictionary value
user_profile["age"] = 23
print("Updated Age:", user_profile["age"])


# Looping through list
print("\nLooping through list:")
for skill in skills:
    print(skill)

# Looping through dictionary
print("\nLooping through dictionary:")
for key, value in user_profile.items():
    print(f"{key} : {value}")
