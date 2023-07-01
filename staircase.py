# Staircase detail
# size n = 4
#       #
#      ##
#     ###
#    ####
# Its base and height are both equal to n . It is drawn using # symbols and spaces. The last line is not preceded by any spaces.

# Write a program that prints a staircase of size .

import math
import os
import random
import re
import sys


def staircase(n):
    for i in range(1, n+1):
        print(" "*(n-i) + "#"*i)


n = 4
staircase(n)
