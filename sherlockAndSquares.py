# Watson likes to challenge Sherlock's math ability. He will provide a starting and ending value that describe a range of integers, inclusive of the endpoints. Sherlock must determine the number of square integers within that range.

# Note: A square integer is an integer which is the square of an integer, e.g. 1, 4, 9, 16, 25.

import math
import os
import random
import re
import sys


def squares(a, b):
    x = math.ceil(math.sqrt(a))
    y = math.floor(math.sqrt(b))
    return y - x + 1


a = 3
b = 9

result = squares(a, b)
print(result)
