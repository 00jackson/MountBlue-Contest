# given a year, y. find the day of the 256th day of that year according to the official Russian calendar during that year. Then print it in the format dd.mm.yyyy, where dd is the two-digit day, mm is the two-digit month, and yyyy is y.
# for example, the given year = 1984. 1984 is divisible by 4, so it is a leap year. The 256th day of a leap year after 1918 is September 12, so the answer is 12.09.1984.

import math
import os
import random
import re
import sys


def dayOfProgrammer(year):
    if year == 1918:
        return "26.09.1918"
    elif (year <= 1917 and year % 4 == 0) or (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        return "12.09.%s" % year
    else:
        return "13.09.%s" % year


year = 2017
result = dayOfProgrammer(year)

print(result)
