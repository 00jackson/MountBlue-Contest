# Given an array of bird sightings where every element represents a bird type id, determine the id of the most frequently sighted type. If more than 1 type has been spotted that maximum amount, return the smallest of their ids.

import math
import os
import random
import re
import sys


def migratoryBirds(arr):
    l = [0] * len(arr)

    for i in range(len(arr)):
        l[arr[i]] += 1

    return l.index(max(l))


arr = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]

result = migratoryBirds(arr)
print(result)
