"""Unit 3 Lesson 2B SANDBOX
CS100: Roadmap to Computing

Do these in order. Type each line yourself - don't copy and paste.
"""

# ---------- Code Along 1: a string is a sequence ----------
word = "python"
print(word[0])              # p     the FIRST letter is index 0
print(word[-1])             # n     index -1 is the LAST letter
print(word[1:4])            # yth   the stop is NOT included
print(len(word))            # 6

# YOUR TURN: add two lines that print
#   the first three letters   -> pyt
#   the last two letters      -> on
print(word[:3])
print(word[-2:])

# ---------- Code Along 2: methods give you a NEW string ----------
name = "  Ada Lovelace  "
print(name.strip())                       # Ada Lovelace
print(name.strip().lower())               # ada lovelace
print(name.strip().replace("a", "A"))     # AdA LovelAce
print(len(name))                          # 16   name itself never changed

# YOUR TURN: split the stripped name into a list and print how many
# words there are  -> 2
name = name.strip()
print(name.split())

# ---------- Code Along 3: count (if you finish early) ----------
# Use .count to print how many times "a" appears in "banana"   -> 3
print("banana".count("a")) #3
print("banana".count("an")) #2
print("banana".count("banana")) #1


# Pattern 1
def count_vowels(word):
    count = 0
    for ch in word:
        if ch in "aeiou":
            count = count + 1
    return count
print(count_vowels("education"))

# Pattern 2
def first_vowel(word):
    for ch in word:
        if ch in "aeiou":
            return ch
    return None
print(first_vowel("hip"))
print(first_vowel("sky"))

# Pattern 3
def reverse_word(word):
    result = ""
    for ch in word:
        result = ch + result
    return result
print(reverse_word("hello"))