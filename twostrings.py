# given two strings, determine if they share a common substring. A substring may be as small as one character.
# For example, the words "a", "and", "art" share the common substring "a". The words "be" and "cat" do not share a substring.


import math
import os
import random
import re
import sys


def twostrings(s1):
    if set(s1) & set(s2):
        return "YES"
    else:
        return "NO"


s1 = input()
s2 = input()

result = twostrings(s1)
print(result)
