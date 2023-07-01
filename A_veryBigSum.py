# In this challenge, you are required to calculate and print the sum of the elements in an array, keeping in mind that some of those integers may be quite large.

import math
import os
import random
import re
import sys


def aVeryBigSum(ar):
    return sum(ar)


ar = [1000000001, 1000000002, 1000000003, 1000000004, 1000000005]

result = aVeryBigSum(ar)
print(result)
