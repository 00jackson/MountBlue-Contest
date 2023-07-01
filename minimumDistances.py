# The distance between two array values is the number of indices between them. Given a, find the minimum distance between any pair of equal elements in the array. If no such value exists, return -1.

import math
import os
import random
import re
import sys


def minimumDistances(a):
    for d in range(1, len(a)):
        for i in range(len(a)-d):
            if a[i] == a[i+d]:
                return d
    return -1


result = minimumDistances([7, 1, 3, 4, 1, 7])
print(result)
