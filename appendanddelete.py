# You have two strings of lowercase English letters. You can perform two types of operations on the first string:
# Append a lowercase English letter to the end of the string.
# Delete the last character of the string. Performing this operation on an empty string results in an empty string.
# Given an integer, k, and two strings, s and t, determine whether or not you can convert s to t by performing exactly k of the above operations on s. If it's possible, print Yes; otherwise, print No.


import math
import os
import random
import re
import sys


def appendanddelete(s, t, k):
    count = 0
    # iterat through the strings and count the number of matching characters
    for i, j in zip(s, t):
        if i == j:
            count += 1
        else:
            break

    t_len = len(t) + (len(s))
    if t_len <= 2*count + k and t_len % 2 == k % 2 or t_len < k:
        return "Yes"
    else:
        return "No"


s = input()
t = input()
k = int(input())
result = appendanddelete(s, t, k)
print(result)
