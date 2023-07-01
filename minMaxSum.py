# Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers. Then print the respective minimum and maximum values as a single line of two space-separated long integers.

import math
import os
import random
import re


def miniMaxSum(arr):
    mini = 9999999999999
    maxi = 0
    s = 0
    n = len(arr)
    for i in range(n):
        s += arr[i]
        mini = min(mini, arr[i])
        maxi = max(maxi, arr[i])

    print(s - maxi, s - mini)


arr = [1, 2, 3, 4, 5]
miniMaxSum(arr)
