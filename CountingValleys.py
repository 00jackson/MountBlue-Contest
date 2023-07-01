#  during the hike he took exactly 'steps' steps. For every step it is indicated if it was an uphill, U, or a downhill, D step. Gary's hikes start and end at sea level and each step up or down represents a 1 unit change in altitude. We define the following terms:
#  - A mountain is a sequence of consecutive steps above sea level, starting with a step up from sea level and ending with a step down to sea level.
#  - A valley is a sequence of consecutive steps below sea level, starting with a step down from sea level and ending with a step up to sea level.

import math
import os
import random
import re
import sys


def countingValleys(n, s):
    valleycount = level = 0
    d = {'U': 1, 'D': -1}  # dictionary to store the value of each step

    for steps in s:
        level += d[steps]
        if level == 0 and steps == 'U':  # if we are at sea level and the step is up, we have completed a valley
            valleycount += 1
    return valleycount


n = 8
s = 'DDUUUUDD'

result = countingValleys(n, s)

print(result)
