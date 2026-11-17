"""Unit 3 Lesson 2C SANDBOX
CS100: Roadmap to Computing

Do these in order. Type each line yourself - don't copy and paste.
"""

# ---------- Code Along 1: keys and values ----------
scores = {"ana": 90, "ben": 75}
print(scores["ana"])   # 90   [ ] with a KEY gives its value
scores["ben"] = 80     # the key exists: change it
scores["cal"] = 60     # a new key: add it
print(scores)          # {'ana': 90, 'ben': 80, 'cal': 60}
print(len(scores))     # 3    pairs, not 6

# YOUR TURN: add "dee" with 85, then print scores["dee"] -> 85


# ---------- Code Along 2: in checks the KEYS ----------
stock = {"apple": 3, "pear": 0}
print("pear" in stock)   # True
print("kiwi" in stock)   # False
print(3 in stock)        # False  3 is a value, not a key

# YOUR TURN: print kiwi's count only if kiwi is a key, else print 0 -> 0


# ---------- Code Along 3: a dictionary in a function ----------
def total(cart):
    result = 0
    for item in cart:              # the loop gives each KEY
        result = result + cart[item]
    return result                  # AFTER the loop


print(total({"pen": 2, "pad": 5}))   # 7

# YOUR TURN: price_of(menu, item) returns the price, or 0 if not on the menu
# menu = {"taco": 3, "soda": 2}
# print(price_of(menu, "taco"))    # 3
# print(price_of(menu, "pizza"))   # 0
def price_of(menu, item):
    if item in menu:
        return menu[item]
    else:
        return 0