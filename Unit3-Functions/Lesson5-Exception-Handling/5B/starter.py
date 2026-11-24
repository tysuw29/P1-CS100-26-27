# Mod Bot - Lesson 5B
# Run the file after every step.

# Given for you - do not change these two lines.
ADMINS = ["Owner", "HeadMod"]
TEST_NAMES = ["Sam", "", "Owner"]


# STEP 1
def kick_user(name, reason):
    if not name:
        raise ValueError("no name")

    # STEP 2
    if name in ADMINS:
        raise ValueError("admin")

    return "Kicked " + name


# STEP 1 TEST
# print(kick_user("Sam", "spam"))


# STEP 2 TEST
# print(kick_user("Owner", "spam"))


# STEP 3
for name in TEST_NAMES:
    try:
        print(kick_user(name, "spam"))
    except ValueError as e:
        print("Failed:", e)