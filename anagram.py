# two words are anagrams of one another if thier letters can be rearranged to form the other word.
# given a string, split it into two contiguous substrings of equal length. determine the minimum number of characters to change to make the two substrings into anagrams of one another.


import math
import os
import re
import sys
import random
from collections import Counter


def anagram(s):
    n = len(s)
    if n % 2 == 1:
        return -1

    s = Counter(s[:n//2]) - Counter(s[n//2:])
    return sum(s.values())


q = int(input().strip())

for q_itr in range(q):
    s = input().strip()
    result = anagram(s)
    print(result)
