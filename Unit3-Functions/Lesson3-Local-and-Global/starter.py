# Lesson 3A - Scope: Score Keeper
# STEP 1 ▸ Run it. Read the error: which line, which name?
# STEP 2 ▸ Pass score in as a parameter. No crash, but is the score right?
# STEP 3 ▸ Return the new score and store it each time.

score = 0


def add_points(points):
    global score
    score = score + points
    print("Inside:", score)
    return score


score = add_points(10)
score = add_points(5)
print("Final score:", score)

# CHECK: Final score: 15
# DONE EARLY: write lose_life(lives) that returns lives - 1.
# Start with lives = 3, call it twice, print lives. Expect: Lives: 1