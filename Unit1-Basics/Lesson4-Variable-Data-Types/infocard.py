"""
Lesson 4 Activity: Student Info Card
CS100: Roadmap to Computing

Build the card shown at the bottom of this file, using your own details.

Everything you need is from today: variables, the four data types,
calculations, type(), and f-strings.

Work top to bottom. Run after every step.
Save before you run. Commit and push when your output matches.
"""

WIDTH = 40


# --- Step 1: your information -----------------------------------
# Fill these in with YOUR details. Keep the types as marked:
# a name is a str, an age is an int, a GPA is a float, and
# honor-student is a bool (True or False, capitalized, no quotes).

my_name = ""                  # str
my_age = 0                    # int
my_gpa = 0.0                  # float
is_honor_student = False      # bool
my_grade = 0                  # int
favorite_subject = ""         # str


# --- Step 2: calculations ---------------------------------------
# Each of these should make a NEW value out of the ones above.
# Do not type the answers in - let Python work them out.

# TODO: age_in_5_years


# TODO: years_until_graduation   (grade 12 minus your grade)


# TODO: age_at_graduation        (use the variable you just made)


# --- Step 3: the card -------------------------------------------
# Borders are WIDTH wide. The title is centered - calculate the
# padding from WIDTH and len(title), don't count spaces.
# Use f-strings for every line that shows a variable.


# --- Step 4: show the types -------------------------------------
# Print the type of four of your variables, plus ONE of your
# calculated values. Use type().
# Look closely at what the calculated one comes out as.


# =============================================================
# TARGET OUTPUT  (yours will show your own details)
# =============================================================
# ========================================
#            STUDENT INFO CARD
# ========================================
# Name: Jordan Rivera
# Age: 16
# Grade: 10
# GPA: 3.75
# Favorite subject: Computer Science
# Honor student: True
# ----------------------------------------
# Age in 5 years: 21
# Years until graduation: 2
# Age at graduation: 18
# ========================================
#
# TYPES USED
# my_name           -> <class 'str'>
# my_age            -> <class 'int'>
# my_gpa            -> <class 'float'>
# is_honor_student  -> <class 'bool'>
# age_in_5_years    -> <class 'int'>


# =============================================================
# STRETCH (optional)
# =============================================================
# Change my_grade to a different year. The card should still work
# and every calculation should update on its own. If you have to
# edit a number anywhere else, you typed an answer instead of
# calculating it.