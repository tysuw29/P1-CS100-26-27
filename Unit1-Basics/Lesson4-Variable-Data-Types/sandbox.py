"""
Lesson 4 SANDBOX
CS100: Roadmap to Computing

Your sandbox for the two Quick Trys during class.

NOT SUBMITTED. Nothing here is graded. Break things, guess, delete,
try again. The graded work is lesson4_infocard_starter.py.
"""


# =============================================================
# QUICK TRY 1 — variables and types
# =============================================================
# These come pre-written. Run them and read the output.

player = "Nova"
level = 12
accuracy = 82.5
is_ranked = True

print(type(player))
print(type(level))
print(type(accuracy))
print(type(is_ranked))
print(type(12))

# TODO: make a variable for your own favourite game and print its type
favorite_game = "Bandit.RIP"
print(type(favorite_game))
print(f"The type of my favorite game {favorite_game} is {type(favorite_game)}")

# TODO: print the type of 42 and the type of 42.0
#       They look the same. They are not.


# =============================================================
# QUICK TRY 2 — conversion
# =============================================================
# Each line below is broken or surprising. Run them one at a time.

# TODO 1: this crashes. Run it, read the error, then fix it with str()
# print("Level " + level)
# print("Level " + level) # will crash
print(f"Level {level}")
print("Level " + str(level))

# TODO 2: predict the output, then run it
# print(10 / 2)
print(1 / 3)
print(8 // 3)

# TODO 3: predict the output, then run it
print(int(3.7))
print(int(9.9))


# TODO 4: this crashes too. Why? What would work instead?
# print(int("3.7"))
print(int("3"))
print(float("3.7"))
print(float("3"))

print(bool(0))
print(bool(1))
print(bool(""))
print(bool([]))
print(bool({}))
print(bool("a" > "z"))