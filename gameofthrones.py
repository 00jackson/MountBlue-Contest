# Given a string, determine if it can be rearranged into a palindrome. Return the string YES or NO.

import math
import os
import random
import re
import sys

from collections import Counter


def gameofthrones(s):
    s = Counter(s)
    total = 0
    for key, value in s.items():
        total += value % 2
    if total > 1:
        return "NO"
    else:
        return "YES"


s = input()
result = gameofthrones(s)
print(result)
