# You are given a number of sticks of varying lengths. You will iteratively cut the sticks into smaller sticks, discarding the shortest pieces until there are none left. At each iteration you will determine the length of the shortest stick remaining, cut that length from each of the longer sticks and then discard all the pieces of that shortest length. When all the remaining sticks are the same length, they cannot be shortened so discard them.
# given the lengths of n sticks print the number of sticks that are left before each iteartration until there are none left.

# arr = [1, 2, 3, 4, 3, 3, 2, 1]

import math
import os
import random
import re
import sys
from collections import Counter


def cutTheSticks(arr):
    result = []
    n = len(arr)
    s = Counter(arr)
    for i in sorted(s):
        result.append(n)
        n -= s[i]  # remove the shorted of an array from the length of the array
    return result


n = int(input().strip())
arr = list(map(int, input().rstrip().split()))
result = cutTheSticks(arr)
print(result)
