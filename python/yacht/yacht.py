"""
This exercise stub and the test suite contain several enumerated constants.

Since Python 2 does not have the enum module, the idiomatic way to write
enumerated constants has traditionally been a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""


# Score categories.
# Change the values as you see fit.
YACHT = 0
ONES = 1
TWOS = 2
THREES = 3
FOURS = 4
FIVES = 5
SIXES = 6
FULL_HOUSE = 7
FOUR_OF_A_KIND = 8
LITTLE_STRAIGHT = 9
BIG_STRAIGHT = 10
CHOICE = 11


def score(dice, category):
    if category == 0:  # Yacht
        return 50 if len(set(dice)) == 1 else 0

    if category in range(1, 7):  # Ones to Sixes
        return category * dice.count(category)

    if category == 7:  # Full House
        counts = {i: dice.count(i) for i in dice}
        if set([2, 3]).issubset(set(counts.values())):
            return sum(dice)
        return 0

    if category == 8:  # Four of a kind
        counts = {i: dice.count(i) for i in dice}
        max_count = max(counts)
        if counts[max_count] >= 4:
            return max_count * 4
        return 0

    if category == 9:  # Little straight
        result = sorted(dice) in [[1, 2, 3, 4, 5]]
        return result * 30

    if category == 10:  # Big straight
        result = sorted(dice) in [[2, 3, 4, 5, 6]]
        return result * 30

    if category == 11:  # Choice
        return sum(dice)
