# a number string s, is beautiful if it can be split into a sequence of two or more positive integers, a[1], a[2], ..., a[n], satisfying the following conditions:
# - a[i] - a[i-1] = 1 for any 1 < i <= n (i.e., each element in the sequence is 1 more than the previous element).
# - No a[i] contains a leading zero. For example, we can split s = 10203 into the sequence {1, 02, 03}, but it is not beautiful because 02 and 03 have leading zeroes.
# - The contents of the sequence cannot be rearranged. For example, we can split s = 312 into the sequence {3, 1, 2}, but it is not beautiful because it breaks our first constraint (i.e., 1 - 3 != 1).
# Perform q queries where each query consists of some integer string s. For each query, print whether or not the string is beautiful on a new line. If it's beautiful, print YES x, where x is the first number of the increasing sequence. If there are multiple such values of x, choose the smallest. Otherwise, print NO.

import math
import os
import random
import re
import sys


def separateNumbers(s):
    if len(s) == 1:
        print('NO')
        return
    else:
        for i in range(1, len(s)//2+1):
            first = s[:i]
            num = int(first)
            while len(first) < len(s):
                next = num + 1
                first += str(next)
                num = next
            if first == s:
                print('YES', s[:i])
                return
        print('NO')


s = '1234'
result = separateNumbers(s)
print(result)
