"""
regular_expressions.py
A beginner-friendly guide demonstrating how to use regular expressions (regex)
in Python with clear explanations and simple, practical examples.

This script covers:
- Basic regex patterns
- Anchors and character classes
- Quantifiers
- Groups, alternations, and lookarounds
- Useful Python functions like search(), findall(), sub(), compile()
"""

import re

# -----------------------------------------------------------
# Basic Examples
# -----------------------------------------------------------

# 1. Check if a string starts with "Hello"
text = "Hello, I am Subham."
pattern = r"^Hello"
match = re.search(pattern, text)
print("Starts with 'Hello':", bool(match))


# 2. Find all digits in a text
text = "My phone number is 8170050382."
digits = re.findall(r"\d", text)
print("Digits found:", digits)


# 3. Extract all words starting with a capital letter
sentence = "Hello, I am Subham and I Live in India."
capital_words = re.findall(r"\b[A-Z][a-zA-Z]*\b", sentence)
print("Capitalized words:", capital_words)


# -----------------------------------------------------------
# Character Classes
# -----------------------------------------------------------

# Find all vowels
text = "Beautiful Day"
vowels = re.findall(r"[aeiouAEIOU]", text)
print("Vowels:", vowels)

# Find characters that are NOT vowels
not_vowels = re.findall(r"[^aeiouAEIOU]", text)
print("Non-vowels:", not_vowels)


# -----------------------------------------------------------
# Quantifiers
# -----------------------------------------------------------

# Match repeated characters
text = "Heeellooo"
repeat = re.findall(r"e+", text)  # one or more 'e'
print("Repeated 'e':", repeat)

nongreedy = re.findall(r"l+?", text)  # non-greedy
print("Non-greedy 'l':", nongreedy)


# -----------------------------------------------------------
# Groups and Alternation
# -----------------------------------------------------------

# Match "cat" or "dog"
animals = re.findall(r"(cat|dog)", "I love my cat and dog.")
print("Animals found:", animals)

# Capture group example (extract username)
email = "user123@gmail.com"
username = re.findall(r"([a-zA-Z0-9._%+-]+)@", email)
print("Username:", username)


# -----------------------------------------------------------
# Lookarounds
# -----------------------------------------------------------

# Positive lookahead: match numbers followed by "kg"
weights = re.findall(r"\d+(?=kg)", "I lifted 20kg and 15kg today.")
print("Weights (kg):", weights)

# Negative lookahead: words NOT followed by a comma
words = re.findall(r"\b\w+\b(?!,)", "Apple, Banana, Mango Orange")
print("Words not followed by comma:", words)


# -----------------------------------------------------------
# Useful Python Regex Functions
# -----------------------------------------------------------

# 1. re.search() – find first match
result = re.search(r"India", "I live in India.")
print("Found 'India' using search():", bool(result))

# 2. re.findall() – find all matches
nums = re.findall(r"\d+", "My numbers are 12, 45, and 100.")
print("Numbers using findall():", nums)

# 3. re.sub() – replace text
cleaned = re.sub(r"\s+", " ", "Python    is     awesome")
print("Cleaned text:", cleaned)

# 4. re.split() – split text using regex
parts = re.split(r"[,; ]+", "apple,banana;orange mango")
print("Split words:", parts)

# 5. re.compile() – store a regex pattern for reuse
pattern = re.compile(r"[A-Za-z]+")
words = pattern.findall("Python3 is amazing!")
print("Words using compiled pattern:", words)

"""
Summary of Common Regex Patterns:
---------------------------------
^         Start of string
$         End of string
.         Any character
\s        Whitespace
\S        Non-whitespace
\d        Digit
\D        Not a digit
\w        Word character
\W        Not a word character
\b        Word boundary
*         0 or more times
+         1 or more times
?         Optional / non-greedy modifier
{n}       Exactly n times
{n,}      At least n times
{n,m}     Between n and m times
[a-z]     Character range
[^a-z]    Negated range
(abc)     Capture group
(?:abc)   Non-capturing group
(a|b)     Alternation
(?=...)   Positive lookahead
(?!...)   Negative lookahead
(?<=...)  Positive lookbehind
(?<!...)  Negative lookbehind
---------------------------------
This file provides the core concepts needed to work with
regular expressions effectively in Python.
"""
