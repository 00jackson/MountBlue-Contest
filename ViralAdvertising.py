# one the first day, half of the 5 people(floor of 5/2 = 2)like the advertisement and each shares it with 3 of their friends. At the beginning of the second day,floor(5/2)*3 = 2*3 = 6 people receive the advertisement.
# each day, floor(recipients/2) of the recipients like the advertisement and will share it with 3 friends on the following day. Assuming nobody receives the advertisement twice, determine how many people have liked the ad by the end of a given day, beginning with launch day as day 1.

import math
import os
import random
import re
import sys


def viralAdvertising(n):
    total_like = 0
    share = 5
    for i in range(n):
        like = math.floor(share/2)
        total_like += like
        share = like * 3
    return total_like


n = 3

result = viralAdvertising(n)
print(result)
