# given an array of integers, find the longest subarray where the absolute difference between any two elements is less than or equal to 1.

import math
import os
import random
import re
import sys


def pickingNumbers(a):
    low = min(a)
    high = max(a)
    a.sort()
    leng = []

    for n in range(low, high+1):
        count = 0
        for num in a:
            if num == n or num == n+1:
                count += 1
                leng.append(count)
    return max(leng)


n = int(input())  # 6
a = list(map(int, input().rstrip().split()))  # [4, 6, 5, 3, 3, 1]
result = pickingNumbers(a)
print(result)
