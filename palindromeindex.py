# given a string of lowercase letters in the rang ascii[a-z], determine the index of a character that can be removed to make the string a palindrome. if the string is already a palindrome, then print -1. there will always be a valid solution, and any correct answer is acceptable. for example, if s = 'bcbc', you can either remove 'b' at index 0 or 'c' at index 3. if s = 'cbb', you can either remove 'b' at index 0 or 'b' at index 2.
# s = "bcbc"
# either remove 'b' at index 0 or 'c' at index 3

import math
import sys
import os
import random
import re


def palindromeIndex(s):
    if s == s[::-1]:
        return -1
    n = len(s)

    for i in range(n//2):
        if s[i] != s[n-i-1]:
            if s[i+1:n-i] == s[i+1:n-i][::-1]:
                return i
            else:
                return n-i-1
    return -1


q = int(input().strip())
for q_itr in range(q):
    s = input().strip()
    result = palindromeIndex(s)
    print(result)
