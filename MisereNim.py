# Two people are playing a game of Misere Nim. The basic rules for this game are as follows:
# The game starts with n piles of stones indexed from 0 to n - 1. Each pile i (where 0 <= i < n) has w[i] stones.
# The players move in alternating turns. During each move, the current player must remove one or more stones from a single pile.
# The player who removes the last stone loses the game.
# Given the value of n and the number of stones in each pile, determine whether the person who wins the game is the first or second person to move. If the first player to move wins, print First; otherwise, print Second. Assume both players move optimally.


import math
import os
import random
import re
import sys
from functools import reduce


def misereNim(s):
    if (set(s) == {1}) and n % 2 == 1:
        return "Second"
    elif (set(s) == {1}) and n % 2 == 0:
        return "First"
    elif reduce((lambda x, y: x ^ y), s):
        return "First"
    else:
        return "Second"


n = int(input())
s = list(map(int, input().rstrip().split()))
result = misereNim(s)
print(result)
