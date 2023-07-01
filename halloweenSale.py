# You wish to buy video games from the famous online video game store Mist.

# Usually, all games are sold at the same price, p dollars. However, they are planning to have the seasonal Halloween Sale next month in which you can buy games at a cheaper price. Specifically, the first game you buy during the sale will be sold at p dollars, but every subsequent game you buy will be sold at exactly d dollars less than the cost of the previous one you bought. This will continue until the cost becomes less than or equal to m dollars, after which every game you buy will cost m dollars each.
# how many games can you buy during the Halloween Sale?

import math
import os
import random
import re
import sys


def howManyGames(p, d, m, s):
    res = 0
    while s >= p:
        res += 1
        s -= p
        p = max(p-d, m)
    return res


p = 20
d = 3
m = 6
s = 80
result = howManyGames(20, 3, 6, 80)
print(result)
