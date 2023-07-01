# little booby loves chocolate. he frequently goes to his favourite 5 & 10 store, penny auntie, to buy them. they are having a promotion at penny auntie. if booby saves enough wrappers, he can turn them in for a free chocolate.
# n = 15, c = 3, m = 2 , answer = 9


import sys
import re
import random
import math
import os


def chocolatefeast(n, c, m):
    choco = n//c  # money to chocolate
    wrap = choco  # chocolate to wrapper

    while wrap >= m:
        choco += wrap//m
        wrap = (wrap//m) + (wrap % m)
    return choco


n = int(input())
c = int(input())
m = int(input())

result = chocolatefeast(n, c, m)
print(result)
