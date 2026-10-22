"""Lesson 8B SANDBOX
CS100: Roadmap to Computing
"""

# ---------- Quick Try 1: a number triangle ----------
# Print this. Each row counts from 1 up to the row number.
#
#   1
#   1 2
#   1 2 3
#   1 2 3 4
for row in range(4):
    for col in range(row + 1):
        print("*", end="")
    print()
    
for row in range(4):
    for col in range(row + 1):
        print(col + 1, end=" ")
    print()

# ---------- Quick Try 2: upside down ----------
# Print a triangle that SHRINKS, starting with 5 stars.
#
#   *****
#   ****
#   ***
#   **
#   *
for row in range(5, 0, -1):
    for col in range(row):
        print("*", end="")
    print()
    
# Break leaves only the inner loop
for row in range(3):
    for col in range(5):
        if col == 2:
            break
        print(row, col)