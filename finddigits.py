# An integer d is a divisor of an integer n if the remainder n % d = 0.
# given an integer, for each digit that makes up the integer determine whether it is a divisor. count the number of divisors occurring within the integer.


import sys
import re
import random
import math
import os


def findDigits(n):
    count = 0
    for i in str(n):
        if int(i) != 0 and n % int(i) == 0:
            count += 1
    return count


t = int(input().strip())
for t_itr in range(t):
    n = int(input().strip())
    result = findDigits(n)
    print(result)
