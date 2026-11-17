"""Unit 3 Lesson 2C Activity - Grade Book
CS100: Roadmap to Computing

Write four functions that take a DICTIONARY and RETURN an answer.
Don't print inside them.

Expected output:

    100
    -1
    270
    True
    False
    {'n': 2, 'o': 2}

Stretch (only when the four above work): curve, at the bottom.
"""


# TASK 1 ▸ look up: check the key with in, then read it
def get_score(scores, name):
    """Return the score for name, or -1 if name is not a key."""
    # TODO: if name is a key in scores, return its score
    # TODO: return -1 - AFTER the if
    pass


# TASK 2 ▸ total: the loop gives you each KEY
def total_points(scores):
    """Return all the scores added together."""
    total = 0
    for name in scores:
        pass  # TODO: add the score for this name - scores[name]
    # TODO: return total - AFTER the loop


# TASK 3 ▸ search: return True inside the loop, False after it
def has_perfect(scores):
    """Return True if any score is 100, otherwise False."""
    for name in scores:
        pass  # TODO: if this name's score is 100, return True right away
    # TODO: return False - AFTER the loop


# TASK 4 ▸ build: an empty dictionary BEFORE the loop
def letter_counts(word):
    """Return a dictionary: each letter of word -> how many times it appears."""
    # Hint: counts = {} first. For each letter: if it is already a key,
    # add 1 to it; otherwise set it to 1. Return AFTER the loop.
    pass


# ---------- TESTS - don't change anything below this line ----------
scores = {"ana": 92, "ben": 100, "cal": 78}
print(get_score(scores, "ben"))
print(get_score(scores, "dee"))
print(total_points(scores))
print(has_perfect(scores))
print(has_perfect({"x": 99}))
print(letter_counts("noon"))


# ---------- STRETCH ----------
# curve(scores, points) returns a NEW dictionary with points added to every
# score, and leaves scores unchanged. Hint: result = {} before the loop.
# def curve(scores, points):
#     ...
# print(curve({"ana": 92, "cal": 78}, 5))   # {'ana': 97, 'cal': 83}
