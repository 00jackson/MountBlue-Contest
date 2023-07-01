# quicksort

import math
import os
import random
import re
import sys


def quicksort(arr):
    left = []
    right = []
    pivot = arr[0]

    for i in range(1, len(arr)):
        if arr[i] < pivot:
            left.append(arr[i])
        else:
            right.append(arr[i])

    return left + [pivot] + right


arr = [5, 2, 8, 9, 1, 3]
print(quicksort(arr))
