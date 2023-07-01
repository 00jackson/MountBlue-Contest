# marc loves cupcakes, but he also likes to stay fit. Each cupcake has a calorie count, and Marc can walk a distance to expend those calories. If Marc has eaten j cupcakes so far, after eating a cupcake with c calories he must walk at least 2^j * c miles to maintain his weight.


import math
import os
import random
import re
import sys


def marcsCakewalk(c):
    miles = 0
    c.sort(reverse=True)
    for i in range(len(c)):
        miles += 2**i * c[i]
    return miles


c = [5, 10, 7]

result = marcsCakewalk(c)

print(result)
