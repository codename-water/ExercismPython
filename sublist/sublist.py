"""
This exercise stub and the test suite contain several enumerated constants.

Enumerated constants can be done with a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

# Possible sublist categories.
# Change the values as you see fit.
SUBLIST = 1
SUPERLIST = 2
EQUAL = 3
UNEQUAL = 0


def sublist(list_one, list_two):
    if list_one == list_two:
        return EQUAL

    s_one = '.'.join(str(i) for i in list_one) + '.'
    s_two = '.'.join(str(i) for i in list_two) + '.'

    if s_two in s_one:
        return SUPERLIST
    if s_one in s_two:
        return SUBLIST
    return UNEQUAL
