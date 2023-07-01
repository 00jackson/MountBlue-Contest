# you are given q queries in the form of x,y and z represents positions for cats A and B, and for mouse C. Complete the function catAndMouse to return the appropriate answer to each query, which will be printed on a new line.
#  - if cat A catches the mouse first print Cat A
#  - if cat B catches the mouse first print Cat B

import math
import os
import random
import re
import sys


def catAndMouse(x, y, z):
    if abs(x-z) < abs(y-z):
        return "Cat A"
    elif abs(x-z) > abs(y-z):
        return "Cat B"
    else:
        return "Mouse C"


x = 1
y = 2
z = 3

result = catAndMouse(x, y, z)
print(result)
