# John Watson knows of an operation called a right circular rotation on an array of integers. One rotation operation moves the last array element to the first position and shifts all remaining elements right one. To test Sherlock's abilities, Watson provides Sherlock with an array of integers. Sherlock is to perform the rotation operation a number of times then determine the value of the element at a given position.

# For each array, perform a number of right circular rotations and return the values of the elements at the given indices.


import math
import os
import random
import re
import sys


def circularArrayRotation(a, k, queries):
    res = []
    n = len(a)
    for i in queries:
        res.append(a[(n-k+i) % n])
    return res


a = [1, 2, 3]
k = 2
queries = [0, 1, 2]

result = circularArrayRotation(a, k, queries)

print(result)
