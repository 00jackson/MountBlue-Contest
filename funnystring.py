# To determine whether a string is funny, create a copy of the string in reverse e.g. abc -> cba. Iterating through each string, compare the absolute difference in the ascii values of the characters at positions 0 and 1, 1 and 2 and so on to the end. If the list of absolute differences is the same for both strings, they are funny.
# determine whether a give string is funny. If it is, return funny, otherwise return not funny.

import os
import sys
import re
import random
import math


def funnystring(s):
    r = s[::-1]  # reverse the string

    for i in range(1, len(s)):
        if abs(ord(s[i]) - ord(s[i-1])) != abs(ord(r[i]) - ord(r[i-1])):
            return "Not Funny"
    return "Funny"


s = input()
result = funnystring(s)
print(result)
