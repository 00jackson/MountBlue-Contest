# Given a square grid of characters in the range ascii[a-z], rearrange elements of each row alphabetically, ascending.
# Determine if the columns are also in ascending alphabetical order, top to bottom. Return YES if they are or NO if they are not.

import math
import os
import random
import re
import sys


def gridChallenge(grid):
    grid = [list(row) for row in grid]
    r = len(grid)
    c = len(grid[0])

    for i in range(r):
        grid[i].sort()

    for j in range(c):
        for i in range(1, r):
            if not grid[i][j] >= grid[i-1][j]:
                return 'NO'
    return 'YES'


grid = ['ebacd', 'fghij', 'olmkn', 'trpqs', 'xywuv']
result = gridChallenge(grid)

print(result)
