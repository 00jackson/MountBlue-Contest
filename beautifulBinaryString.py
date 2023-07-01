# alice has a binary string. she thinks a binary string is beautiful if and only if it doesn't contain the substring '010'.
# in one step, alice can change a 0 to a 1 or vice versa. count and print the minimum number of steps needed to make alice see the string as beautiful.


import math
import os
import random
import re
import sys


def beautifulBinaryString(b):
    return b.count('010')


b = '0101010'
result = beautifulBinaryString(b)

print(result)
