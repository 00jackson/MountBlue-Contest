# Consider an array of numeric strings where each string is a positive number with anywhere from 1 to 10^6 digits. Sort the array's elements in non-decreasing, or ascending order of their integer values and print each element of the sorted array on a new line.

import math
import os
import random
import re
import sys


def bigSorting(unsorted):
    unsorted.sort(key=lambda x: (len(x), x))
    return unsorted


unsorted = ['31415926535897932384626433832795', '1', '3', '10', '3', '5']
result = bigSorting(unsorted)

print(result)
