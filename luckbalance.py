# lena is preparing for an important coding competition that is preceded by a number of sequential preliminary contests. initially, her luck balance is 0. she believes in "saving luck", and wants to check her theory. each contest is described by two integers, l[i] and t[i]:
# L[i] is the amount of luck associated with a contest. if Lena wins the contest, her luck balance will decrease by L[i]; if she loses it, her luck balance will increase by L[i].
# T[i] denotes the contest's importance rating. it's equal to 1 if the contest is important, and it's equal to 0 if it's unimportant.
# if lena loses no more than k important contests, what is the maximum amount of luck she can have after competing in all the preliminary contests? this value may be negative.


import sys
import os
import math
import re
import random


def luckbalance(k, contests):
    contest = {}  # dictionary to store the luck and importance of each contest

    for l, c in contests:
        if c not in contest:
            contest[c] = [l]  # if the contest is not in the dictionary, add it
        else:
            # if the contest is in the dictionary, append it
            contest[c].append(l)

    luck = 0  # initialize luck to 0
    if 0 in contest:
        luck += sum(contest[0])  # add all the unimportant contests to luck
    if 1 in contest:
        # sort the important contests in descending order
        s = sorted(contest[1], reverse=True)
        luck += sum(s[:k])  # add the first k important contests to luck
        # subtract the remaining important contests from luck
        luck -= sum(s[k:])

    return luck


n = int(input())
k = int(input())
contests = []
for _ in range(n):
    contests.append(list(map(int, input().rstrip().split())))
result = luckbalance(k, contests)
print(result)
