# Given an array of stick lengths, use 3 of them to construct a non-degenerate triange with the maximum possible perimeter. Print the lengths of its sides as 3 space-separated integers in non-decreasing order.

# If there are several valid triangles having the maximum perimeter:
# - Choose the one with the longest maximum side.
# - If more than one has that maximum, choose from them the one with the longest minimum side.
# - If more than one has that maximum as well, print any one them.
# If no non-degenerate traingle exists,return [-1]


import math
import os
import random
import re
import sys


def maximumPerimeterTriangle(sticks):
    sticks.sort()
    i = len(sticks) - 3
    while i >= 0 and sticks[i] + sticks[i+1] <= sticks[i+2]:
        i -= 1
    if i >= 0:
        return [sticks[i], sticks[i+1], sticks[i+2]]
    else:
        return [-1]


sticks = [1, 1, 1, 3, 3]
result = maximumPerimeterTriangle(sticks)

print(result)
