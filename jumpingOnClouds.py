# There is an array of clouds, c and an energy level e = 100. The size of the jump is k. If c[i] = 1, then it is a thundercloud and she loses 2 units of energy. Otherwise, she loses 1 unit of energy. The game ends when she lands back on cloud 0.
# given the values of n, k, and the configuration of the clouds as an array c, determine the final value of e after the game ends.


import math
import os
import random
import re
import sys


def jumpingOnClouds(c, k):
    n = len(c)
    energy = 100
    i = 0
    while True:
        energy = energy - 1 - 2 * c[i]
        i = (i + k) % n
        if i == 0:
            break
    return energy


c = [0, 0, 1, 0]
k = 2
result = jumpingOnClouds(c, k)

print(result)
