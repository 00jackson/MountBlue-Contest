# there is a new mobile game that starts with consecutively numbered clouds. Some of the clouds are thunderheads and others are cumulus. The player can jump on any cumulus cloud having a number that is equal to the number of the current cloud plus 1 or 2. The player must avoid the thunderheads. Determine the minimum number of jumps it will take to jump from the starting postion to the last cloud. It is always possible to win the game.
# for each game, you will get an array of clouds numbered 0 if they are safe or 1 if they must be avoided.

import random
import re
import os
import math
import sys
c = [0, 0, 1, 0, 0, 1, 0]


def jumpingonclouds(c):
    stepCount = -1
    currentIndex = 0

    while currentIndex < len(c):
        try:
            currrentIndex += 2 if c[currentIndex + 2] == 0 else 1
        except:
            currentIndex += 1
        stepCount += 1
    return stepCount


c = [0, 0, 1, 0, 0, 1, 0]
result = jumpingonclouds(c)
print(result)
