# the fee structure is as follows:
#  1. If the book is returned on or before the expected return date, no fine will be charged (i.e.: fine = 0).
#  2. If the book is returned after the expected return day but still within the same calendar month and year as the expected return date, fine = 15 Hackos * (the number of days late).
#  3. If the book is returned after the expected return month but still within the same calendar year as the expected return date, the fine = 500 Hackos * (the number of months late).
#  4. If the book is returned after the calendar year in which it was expected, there is a fixed fine of 10000 Hackos.
#  charges are based only on the least precise measure of lateness. For example, whether a book is due January 1, 2017 or December 31, 2017, if it is returned January 1, 2018, that is a year late and the fine would be 10000 Hackos.

import math
import os
import random
import re
import sys


def libraryFine(d1, m1, y1, d2, m2, y2):
    if y1 < y2:
        return 0
    elif y1 == y2:
        if m1 < m2:
            return 0
        elif m1 == m2:
            if d1 <= d2:
                return 0
            else:
                return 15 * (d1 - d2)
        else:
            return 500 * (m1 - m2)
    else:
        return 10000


d1 = 9
d2 = 6
m1 = 6
m2 = 6
y1 = 2015
y2 = 2015

result = libraryFine(d1, m1, y1, d2, m2, y2)
print(result)
