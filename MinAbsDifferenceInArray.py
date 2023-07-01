# the absolute difference between two values a and b is written as |a - b| or |b-a| and they are equal. if a = 3 and b = 2, |3-2| = |2-3| = 1.
# given an array of integers, find the minimum absolute difference between any two elements in the array.


import math
import os
import random
import re
import sys


def minimumAbsoluteDifference(arr):
    arr.sort()
    diff = abs(arr[0] - arr[1])
    for i in range(len(arr) - 1, 0, -1):
        if abs(arr[i] - arr[i-1]) < diff:
            diff = abs(arr[i] - arr[i-1])
    return diff


arr = [3, -7, 0]

result = minimumAbsoluteDifference(arr)
print(result)
