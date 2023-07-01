# Two children, Lily and Ron, want to share a chocolate bar. Each of the squares has an integer on it.

# Lily decides to share a contiguous segment of the bar selected such that:

# - The length of the segment matches Ron's birth month, and,
# - The sum of the integers on the squares is equal to his birth day.
# - Determine how many ways she can divide the chocolate.

import math
import os
import random
import re
import sys


def birthday(s, d, m):
    i = 0
    j = m
    count = 0

    while j <= len(s):
        if sum(s[i:j]) == d:
            count += 1
        i += 1
        j += 1
    return count


s = [1, 2, 1, 3, 2]
d = 3
m = 2

result = birthday(s, d, m)
print(result)
