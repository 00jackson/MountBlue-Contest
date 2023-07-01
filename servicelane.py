# A driver is driving on the freeway. The check engine light of his vehicle is on, and the driver wants to get service immediately. Luckily, a service lane runs parallel to the highway. It varies in width along its length.
# You will be given an array of widths at points along the road (indices), then a list of the indices of entry and exit points. Considering each entry and exit point pair, calculate the maximum size vehicle that can travel that segment of the service lane safely.

import math
import os
import random
import re
import sys


def servicelane(n, cases):
    res = []
    for i, j in cases:
        res.append(min(width[i:j + 1]))

    return res


width = list(map(int, input().split()))
n = int(input().split()[1])
cases = []
