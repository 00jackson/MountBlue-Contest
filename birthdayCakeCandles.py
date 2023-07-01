# You are in charge of the cake for a child's birthday. You have decided the cake will have one candle for each year of their total age. They will only be able to blow out the tallest of the candles. Count how many candles are tallest.

import math
import os
import random
import re
import sys


def birthdaycakeCandles(candles):
    n = len(candles)
    maxi = 0
    count = 0
    for i in range(n):
        if candles[i] > maxi:
            maxi = candles[i]
            count = 1
        elif candles[i] == maxi:
            count += 1
    return count


n = 4
candles = [4, 4, 1, 3]
result = birthdaycakeCandles(candles)
print(result)
