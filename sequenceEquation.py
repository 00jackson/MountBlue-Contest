# given a sequence of n integers p(1), p(2),...,p(n) where each element is distinct and satisfies 1<=p(x)<=n. For each x where 1<=x<=n, that is x increaments from 1 to n, find any integer y such that p(p(y)) = x and keep a history of the values of y in a return array.


import math
import os
import random
import re
import sys


def permutationEquation(p):
    res = []
    n = len(p)
    for i in range(1, n+1):
        res.append(p.index(p.index(i)+1)+1)
    return res


p = [4, 3, 5, 1, 2]

result = permutationEquation(p)
print(result)
