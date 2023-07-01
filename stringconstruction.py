# amanda has string of lowercase letters thats she wants to copy to a new string. she can perform the following operations with the given costs. she can perform them any number of times to construct a new string p:
# append a character to the end of string p at a cost of 1 dollar.
# choose any substring of p and append it to the end of p at no charge.
# given n strings s[i], find and print the minimum cost of copying each s[i] to p[i] on a new line.

import math
import sys
import re
import random
import sys


def stringconstruction(s):
    return len(set(s))


q = int(input().strip())
for a0 in range(q):
    s = input().strip()
    result = stringconstruction(s)
    print(result)
