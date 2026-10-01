"""Lesson 6A Activity - Training Log
CS100: Roadmap to Computing

Ask how many rounds, then print one line per round.

  Damage goes up each round:  round 1 is 10, round 2 is 20, and so on.

Your output for 4 rounds should look like this:

    ========================
       TRAINING LOG
    ========================
    Round 1 - 10 damage
    Round 2 - 20 damage
    Round 3 - 30 damage
    Round 4 - 40 damage
    ========================
    4 rounds completed

And for 1 round:

    ========================
       TRAINING LOG
    ========================
    Round 1 - 10 damage
    ========================
    1 rounds completed
"""

LINE = "========================"


# TODO 1: ask how many rounds, and convert it with int()


# TODO 2: print the header - LINE, the title, LINE again.
#         This happens ONCE, before any round.


# TODO 3: write a for loop that runs once per round.
#         Use range().


# TODO 4: inside the loop, print one line per round:
#             Round 1 - 10 damage
#
#         Careful: range() starts counting at 0, and there is no
#         "Round 0". Work out what you have to add.


# TODO 5: after the loop, print LINE and then how many rounds were
#         completed. These two lines must print ONCE, not once per
#         round. The only thing that decides that is indentation.


# ---------- TEST BEFORE YOU SUBMIT ----------
# Run it with 4, then with 1, then with 0.
#
# With 0 rounds you should still get the header and the footer, and
# no round lines at all. If your program crashes or skips the header,
# something is in the wrong place.
