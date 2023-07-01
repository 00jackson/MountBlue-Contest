# Reduce a string of lowercase characters in range ascii[‘a’..’z’]by doing a series of operations. In each operation, select a pair of adjacent letters that match, and delete them.
# Delete as many characters as possible using this method and return the resulting string. If the final string is empty, return Empty String

import math
import os
import random
import re
import sys


def superReducedString(s):
    # Write your code here
    result = []
    for i in range(len(s)):
        if len(result) == 0 or result[-1] != s[i]:
            result.append(s[i])

        else:
            result.pop()
    if len(result) == 0:
        return "Empty String"
    else:
        return "".join(result)


s = "aabccdd"

output = superReducedString(s)
print(output)
