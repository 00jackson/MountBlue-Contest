# You are choreographing a circus show with various animals. For one act, you are given two kangaroos on a number line ready to jump in the positive direction (i.e, toward positive infinity).

# The first kangaroo starts at location x1 and moves at a rate of v1 meters per jump.
# The second kangaroo starts at location x2 and moves at a rate of v2 meters per jump.
# You have to figure out a way to get both kangaroos at the same location at the same time as part of the show. If it is possible, return YES, otherwise return NO.


import math
import os
import random
import re
import sys


def kangaroo(x1, v1, x2, v2):
    if x1 < x2 and v1 < v2:
        return "NO"
    else:
        if v1 != v2 and (x2 - x1) % (v1 - v2) == 0:
            return "YES"
        else:
            return "NO"


# Sample input
x1 = 0
v1 = 3
x2 = 4
v2 = 2

# Call the kangaroo function
result = kangaroo(x1, v1, x2, v2)

# Print the result
print(result)
