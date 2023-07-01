# The website considers a password to be strong if it satisfies the following criteria:
# - Its length is at least 6.
# - It contains at least one digit.
# - It contains at least one lowercase English character.
# - It contains at least one uppercase English character.
# - It contains at least one special character. The special characters are: !@#$%^&*()-+


import math
import os
import random
import re
import sys


def minimumNumber(n, password):
    n = len(password)
    spl = "!@#$%^&*()-+"
    l = [0, 0, 0, 0]

    for char in password:
        if char.isdigit():
            l[0] = 1
        elif char.islower():
            l[1] = 1
        elif char.isupper():
            l[2] = 1
        elif char in spl:
            l[3] = 1
    return max(6-n, 4-sum(l))


n = 11
password = "#HackerRank"
result = minimumNumber(n, password)

print(result)
