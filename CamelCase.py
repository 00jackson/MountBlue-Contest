# There is a sequence of words in CamelCase as a string of letters, s, having the following properties:

# - It is a concatenation of one or more words consisting of English letters.
# - All letters in the first word are lowercase.
# - For each of the subsequent words, the first letter is uppercase and rest of the letters are lowercase.
# Given s, determine the number of words in s.

import math
import os
import random
import re
import sys


def CamelCase(s):
    count = 1
    for word in s:
        if word.isupper():
            count += 1
    return count


s = "saveChangesInTheEditor"
result = CamelCase(s)

print(result)
