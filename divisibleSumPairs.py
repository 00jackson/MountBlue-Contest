# given an array of integers and a positive integer k, determine the number of (i, j) pairs where i < j and ar[i] + ar[j] is divisible by k.

import math
import os
import random
import re
import sys


def divisibleSumPairs(n, k, ar):
    ar.sort()
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            if (ar[i] + ar[j]) % k == 0:
                count += 1
    return count


ar = [1, 3, 2, 6, 1, 2]
k = 3
n = len(ar)

result = divisibleSumPairs(n, k, ar)
print(result)
