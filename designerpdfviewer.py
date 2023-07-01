# when a contiguous block of text is selected in a pdf viewer, the selection is highlighted with a blue rectangle. In this PDF viewer, each word is highlighted independently. For example:
# there is a list of 26 character of height aligned by index to their letters.For example, 'a' is at index 0 and is at index 25. there will also be a string. Using the letter heights given, determine the area of the rectangle highlight in mm2 assuming all letters are 1mm wide.

# h = [1 3 1 3 1 4 1 3 2 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5]
# word = 'abc'


import math
import os
import random
import re
import sys


def designerpdfviewer(h, word):
    height = 0
    for letter in word:
        height = max(height, h[ord(letter) - ord('a')])

    return height * len(word)


h = list(map(int, input().rstrip().split()))
word = input()
result = designerpdfviewer(h, word)
print(result)
