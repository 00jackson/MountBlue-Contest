# there is a collection of rocks where each rock has various minerals embeded in it. Each type of mineral is designated by a lowercase letter in the range ascii[a-z]. There may be multiple occurrences of a mineral in a rock. A mineral is called a gemstone if it occurs at least once in each of the rocks in the collection.
# given a list of minerals embedded in each of the rocks, display the number of types of gemstones in the collection.

# arr = [ 'abcdde', 'baccd', 'eeabg' ] # 2

import math
import os
import random
import re
import sys


def gemstones(arr):
    res = set(arr[0])
    for i in range(1, len(arr)):
        temp = set(arr[i])
        # intersection of two sets is the set of elements that are common to both sets
        res = res.intersection(temp)
    return len(res)


n = int(input())
arr = []
for _ in range(n):
    arr_item = input()
    arr.append(arr_item)
result = gemstones(arr)
print(result)
