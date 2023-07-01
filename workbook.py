# lisa just got a new math workbook. A workbook contains exercise problems, grouped into chapters.
# lisa believes a problem to be special if its index (within a chapter) is the same as the page number where it's located. The format of lisa's book is as follows:
# there are n chapters in lisa's workbook, numbered from 1 to n.
# the nth chapter has arr[n] problems, numbered from 1 to arr[n].
# each page can hold up to k problems. Only a chapter's last page of exercises may contain fewer than k problems.
# each new chapter starts on a new page, so a page will never contain problems from more than one chapter.
# the page number indexing starts at 1.
# given the details for lisa's wrorkbook, can you count its number of special problems?


import math
import os
import random
import re
import sys


def workbook(n, k, arr):
    ans = 0
    page = 1
    for probs in arr:
        for index in range(1, probs+1):
            if index == page:
                ans += 1
            if index == probs or index % k == 0:
                page += 1
    return ans


n = int(input())
k = int(input())
arr = list(map(int, input().rstrip().split()))
result = workbook(n, k, arr)
print(result)
