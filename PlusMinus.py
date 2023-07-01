# Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero. Print the decimal value of each fraction on a new line with 6 places after the decimal.
import math
import os
import random
import re
import sys


def plusMinus(arr):

    pos = neg = zero = 0
    n = len(arr)

    for i in range(n):
        if arr[i] == 0:
            zero += 1
        elif arr[i] > 0:
            pos += 1
        else:
            neg += 1

    print(pos/n)
    print(neg/n)
    print(zero/n)


arr = [-1, 2, 0, -3, 0, 5, 6]

plusMinus(arr)
