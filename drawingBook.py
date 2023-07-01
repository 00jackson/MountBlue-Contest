# when they open a page, page number 1 is always on the right side
# when they flip page 1, they see pages 2 and 3. If they flip page 2, they see pages 4 and 5
#  and so on. Given n and p, find and print the minimum number of pages Brie must turn in order to arrive at page p.

import math
import os
import random
import re


def pageCount(n, p):
    l = p//2
    n = n+1 if n % 2 == 0 else n
    r = (n-p)//2

    return min(l, r)


n = 6
p = 2

result = pageCount(n, p)
print(result)
