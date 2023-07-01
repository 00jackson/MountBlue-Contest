# A person wants to determine the most expensive computer keyboard and USB drive that can be purchased with a give budget. Given price lists for keyboards and USB drives and a budget, find the cost to buy them. If it is not possible to buy both items, return -1.

import os
import sys


def getMoneySpent(keyboards, drives, b):
    # Write your code here
    max = -1
    for i in keyboards:
        for j in drives:
            if i + j <= b and i + j > max:
                max = i + j
    return max


keyboards = [3, 1]
drives = [5, 2, 8]
b = 10

result = getMoneySpent(keyboards, drives, b)
print(result)
