# Given an array of integers, determine the minimum number of elements to delete to leave only elements of equal value.

import math
import os
import random
import re
import sys
from collections import Counter


def equalizeArray(arr):
    c = Counter(arr)
    return len(arr) - max(c.values())


result = equalizeArray([3, 3, 2, 1, 3])
print(result)
