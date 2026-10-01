"""Lesson 6A Sandbox
CS100: Roadmap to Computing
"""

# ---------- Quick Try 1: what does range give you? ----------
for i in range(5):
    print(i)


# ---------- Quick Try 2: the loop variable is real ----------
# Print the round number and the damage for each round.
# Damage is 10 times the round number.
#
# Careful: range(4) starts at 0, but there is no "Round 0".
for i in range(4):
    print(f"Round {i+1} - {(i+1)*10} damage")

# ---------- Try it: inside or outside? ----------
# Move the "Match over" line so it prints ONCE, at the end.
# Then move it back so it prints after every round.
# What is the only thing you changed?


# for i in range(3):
#     print("Fighting...")
#     print("Match over")

for i in range(3):
    print("Fighting...")
    for j in range(4):
        print("Match over")