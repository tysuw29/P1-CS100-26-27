"""Lesson 8A SANDBOX
CS100: Roadmap to Computing
"""

# ---------- Quick Try 1: a grid of # ----------
# Print 3 rows of 5 # signs, using a loop inside a loop.
# Use  print("#", end="")  for each sign, and  print()  to end each row.
#
#   #####
#   #####
#   #####
for row in range(3):
    for col in range(5):
        print("#", end="")
    print()

# ---------- Quick Try 2: a times table ----------
# Print the 5 x 5 times table. Each row is one number times 1 to 5.
# Use  print(row * col, end=" ")  inside, and  print()  after the inner loop.
