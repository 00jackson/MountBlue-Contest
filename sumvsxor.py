# given an integer n, find each x such that:
# 0 <= x <= n
# n + x = n ^ x
# where ^ denotes the bitwise XOR operator. Then print an integer denoting the total number of x's satisfying the criteria above.


import math
import os
import random
import re
import sys


def sumxor(n):
    result = 1
    while n:
        b = n & 1
        n >>= 1  # divide by 2
        if b == 0:
            result *= 2
    return result


n = int(input())
result = sumxor(n)
print(result)
