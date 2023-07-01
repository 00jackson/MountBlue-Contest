# given a sequence of integers a, a triplet (a[i], a[j], a[k]) is beautiful if:
#  i < j < k
#  a[j] - a[i] = a[k] - a[j] = d
# given an increasing sequence of integers and the value of d, count the number of beautiful triplets in the sequence.


import math
import sys
import random
import re
import os
from collections import Counter


def beautifulTriplets(d, arr):
    m = Counter(arr)
    count = 0
    for i in arr:
        if m[i + d] and m[i + 2*d]:
            count += 1

    return count


d = int(input())  # 3
arr = list(map(int, input().rstrip().split()))  # [1, 2, 4, 5, 7, 8, 10]

result = beautifulTriplets(d, arr)
print(result)
