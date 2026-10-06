"""Lesson 6C Sandbox - practice file, not submitted, not graded.
CS100: Roadmap to Computing
"""

# ---------- Quick Try 1: letter by letter ----------
# Print your own first name, ONE CHARACTER PER LINE.
# Use a for-loop over the string, and print the LOOP VARIABLE.
for char in "skibidi":
    print(char)

# ---------- Quick Try 2: vowel counter ----------
# Ask the user for a word, then count how many vowels it has
# (a, e, i, o, u - lowercase only, that is today's rule).
# Print the count AFTER the loop, once.
#
word = input("Enter a word: ")
vowels = 0
for char in word:
    if char in "aeiou":
        vowels += 1
print(vowels)

# Remember the three places from 6B:
#   counter before the loop - update inside - use after
word = "bergen"
for i in range(len(word)):
    print(word[i])


# ---------- Break it on purpose ----------
# Quick Try 2 again, but with the counter created INSIDE the loop.
# Run it with a word. Then run it again by pressing Enter (empty word).
# Write down what happened both times, and why.
consonants = 0
digits = 0
if "a" <= char <= "z":
   consonants += 1
if "0" <= char <= "9":
    digits += 1
# ---------- Stretch (optional): reversed ----------
# Build a reversed copy of the word: put each new character on the
# LEFT of what you have so far. Start from an empty string.
