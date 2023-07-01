# A pangram is a string that contains every letter of the alphabet. Given a sentence determine whether it is a pangram in the English alphabet.
# Ignore case. Return either pangram or not pangram as appropriate.


import math
import os
import random
import re
import sys


def pangrams(s):
    temp = set(s.lower()) - set(' ')
    if len(temp) == 26:
        return 'pangram'
    else:
        return 'not pangram'


s = 'We promptly judged antique ivory buckles for the next prize'
result = pangrams(s)

print(result)
