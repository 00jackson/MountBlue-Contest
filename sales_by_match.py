# There is a large pile of socks that must be paired by color.
# Given an array of integers representing the color of each sock, determine how many pairs of socks with matching colors there are.
import math
import os
import random
import sys


def sockMerchant(n, ar):
    # dict of count of each color
    count = {}
    for n in ar:
        if n in count:
            count[n] += 1
        else:
            count[n] = 1
    # count the pairs
    pairs = 0
    for c in count.values():
        # segregate
        pairs += math.floor(c/2)
    return pairs


# Test case
n = 9
ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]

# Call the sockMerchant function
result = sockMerchant(n, ar)

# Print the result
print("Number of pairs:", result)
