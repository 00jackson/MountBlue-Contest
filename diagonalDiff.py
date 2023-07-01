# Given a square matrix, calculate the absolute difference between the sums of its diagonals.

import math
import os
import random
import re
import sys


def diagonalDiff(arr):
    n = len(arr)
    leftdiag = rightdiag = 0

    for i in range(n):
        leftdiag += arr[i][i]
        rightdiag += arr[i][n-i-1]

    return abs(leftdiag - rightdiag)


arr = [[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]]

result = diagonalDiff(arr)
print(result)
