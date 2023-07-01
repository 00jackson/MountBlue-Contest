# A decent number has the following porperties:
# - Its digits can only be 3's and/or 5's.
# - The number of 3's it contains is divisible by 5.
# - It is largest such number for its length.
#  for example, the numbers 55533333 and 555555 are decent numbers, but 333333 and 55555 are not.

import math
import os
import random
import re
import sys


def decentNumber(n):
    m = n
    while m % 3 != 0:
        m -= 5
    if m < 0:
        print(-1)
    else:
        print(m * '5' + (n - m) * '3')


t = int(input().strip())
for t_itr in range(t):
    n = int(input().strip())
    result = decentNumber(n)
    print(result)
