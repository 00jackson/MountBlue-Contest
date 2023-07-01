# player 1 always makes moves first.and both players always play optimally.The rules of the game are as follows:
# - initially there are n towers.
# - each tower is of height m.
# - the players move in alternating turns.
# - each turn, a player can choose a tower of height x and reduce its height to y, where 1 <= y < x and y evenly divides x.
# - if the curr player can choose a tower with 0 height, they lose.
# given the values of n and m, determine which player will win. If the first player wins, return 1. Otherwise, return 2.


import math
import os
import random
import re
import sys


def towerBreakers(n, m):
    return 2 if n % 2 == 0 or m == 1 else 1


n = 2
m = 100

result = towerBreakers(n, m)
print(result)
