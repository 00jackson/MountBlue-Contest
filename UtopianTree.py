# the utopian tree goes through 2 cycles of growth every year. each spring, it doubles in height. each summer, it grows 1 meter.
# a utopian tree sapling with a height of 1 meter is planted at the onset of spring. how tall will the tree be after n growth cycles?
#  for example, if the number of growth cycles is n = 5, the calculations are as follows:
# Period  Height
# 0          1
# 1          2
# 2          3
# 3          6
# 4          7
# 5          14


import math
import os
import random
import re
import sys


def utopianTree(n):
    s = 0
    for i in range(n+1):
        s = s+1 if i % 2 == 0 else s*2
    return s


n = int(input())
result = utopianTree(n)
print(result)
