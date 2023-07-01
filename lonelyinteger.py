# Given an array of integers, where all elements but one occur twice, find the unique element.

import math
import os
import random
import re
import sys


def lonelyinteger(a):
    for i in a:
        if a.count(i) == 1:
            return i
    return None


a = list(map(int, input().rstrip().split()))
result = lonelyinteger(a)
print(result)
