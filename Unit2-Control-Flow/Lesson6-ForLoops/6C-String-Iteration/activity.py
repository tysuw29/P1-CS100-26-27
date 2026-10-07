"""Lesson 6C Activity - Text Analyzer
CS100: Roadmap to Computing

Ask the user for a line of text, then report how many vowels,
consonants, digits, spaces, and other characters it contains -
in ONE pass through the text.

Expected output:

    Enter text: code 4 u
    ================
      TEXT ANALYZER
    ================
    Vowels:     3
    Consonants: 2
    Digits:     1
    Spaces:     2
    Other:      0
    ================

Rubric:
    1. Five counters created BEFORE the loop
    2. One for-loop over the text - a single pass
    3. An if / elif chain: vowels first, then a-z, then 0-9,
       then space, then else
    4. Report printed once, AFTER the loop
"""

LINE = "================"

# TODO 1: Ask the user for a line of text and store it in `text`.
text = input("Enter text: ")

# TODO 2: Create five counters, all starting at 0:
#         vowels, consonants, digits, spaces, other
vowels = 0
consonants = 0
digits = 0
spaces = 0
other = 0

# TODO 3: Loop over the text, one character at a time.
for char in text:
    if char in "aeiou":
        vowels += 1
    elif char >= "a" and char <= "z":
        consonants += 1
    elif char >= "0" and char <= "9":
        digits += 1
    elif char == " ":
        spaces += 1
    else:
        other += 1

    # TODO 4: if the character is a vowel, count it as a vowel.
    # TODO 5: elif it is a lowercase letter, count it as a consonant.
    # TODO 6: elif it is a digit, count it as a digit.
    # TODO 7: elif it is a space, count it as a space.
    # TODO 8: otherwise, count it as other.


# TODO 9: Print the report - header, five counts, footer - once.
print(LINE)
print("  TEXT ANALYZER")
print(LINE)
print(f"Vowels:     {vowels}")
print(f"Consonants: {consonants}")
print(f"Digits:     {digits}")
print(f"Spaces:     {spaces}")
print(f"Other:      {other}")
print(LINE)
