# Lily likes to play games with integers. She has created a new game where she determines the difference between a number and its reverse. For instance, given the number 12, its reverse is 21. Their difference is 9. The number 120 reversed is 21, and their difference is 99.
# she decides to apply her game to decision making. She will look at a numbered range of days and will only go to a movie on a beautiful day.
# given a range of numbered days, [i...j] and a number k, determine the number of days in the range that are beautiful. Beautiful numbers are defined as numbers where |i - reverse(i)| is evenly divisible by k. If a day's value is a beautiful number, it is a beautiful day. Print the number of beautiful days in the range.

import math
import os
import random
import re
import sys


def beautifulDays(i, j, k):
    count = 0
    for day in range(i, j+1):
        if abs(day - int(str(day)[::-1])) % k == 0:
            count += 1
    return count


i = 20
j = 23
k = 6

result = beautifulDays(i, j, k)

print(result)
