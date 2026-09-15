"""
Lesson 5 SANDBOX
CS100: Roadmap to Computing
"""


# =============================================================
# QUICK TRY 1 — input() and conversion
# =============================================================
# Run this. Type a number when it asks. Then read the error.

age = input("Your age: ")
print(int(age) + 1)


# TODO: fix the line above so it prints your age plus one.


# TODO: ask for a price and convert it properly.
#       A price is not a whole number.
price = input("Enter a price: ")
print(float(price) + 1.00)

# =============================================================
# QUICK TRY 2 — operators
# =============================================================
# Predict each answer BEFORE you run it.

print(17 / 5)
print(17 // 5)
print(17 % 5)
print(2 ** 5)


# TODO: 17 slices, 5 people. Print how many each person gets
#       and how many are left over.
slices = 17
people = 5
print(slices // people)
print(slices % people)

# TODO: predict this one, then run it. It surprises people.
# print(-7 % 3)
print(-7 % 3)