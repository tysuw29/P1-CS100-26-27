# Lesson 4A - None, False and 0: Gradebook Lookup
# STEP 1 ▸ Run it. Zoe took the quiz and got 0. Why does it say not found?
# STEP 2 ▸ Fix report: check for None with is None.
# STEP 3 ▸ Write is_passing(score): True at 65 or more, else False.

scores = {"Ana": 92, "Ben": 58, "Zoe": 0}


def find_score(scores, name):
    """Return the name's score, or None if they are not listed."""
    return scores.get(name, None)


def is_passing(score):
    """Return True if the score is 65 or more, else False."""
    return score is not None and score >= 65


def report(name):
    score = find_score(scores, name)
    if score is None:
        print(name, "not found")
    else:
        p = is_passing(score)
        print(name, score, "passing", p)


report("Ana")
report("Zoe")
report("Max")

# CHECK: Ana 92 passing: True / Zoe 0 passing: False / Max not found
# DONE EARLY: write average(scores): None for an empty dict, else the mean.
# print("Average:", average(scores)) and print("Empty:", average({}))
# Expect: Average: 50.0 then Empty: None
