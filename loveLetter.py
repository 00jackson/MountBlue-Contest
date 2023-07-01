# James found a love letter that his friend Harry has written to his girlfriend. James is a prankster, so he decides to meddle with the letter. He changes all the words in the letter into palindromes.
# To do this, he follows two rules:
# - He can only reduce the value of a letter by 1, i.e. he can change d to c, but he cannot change c to d or d to b.
# - The letter a may not be reduced any further.
# each reduction in the value of any letter is counted as a single operation. Find the minimum number of operations required to convert a given string into a palindrome.


import math
import os
import random
import re
import sys


def theLoveLetterMystery(s):
    count = 0
    n = len(s)
    for i in range(len(s)//2):
        count += abs(ord(s[i]) - ord(s[n-i-1]))
    return count


result = theLoveLetterMystery('abc')
print(result)
