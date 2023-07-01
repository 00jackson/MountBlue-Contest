# A modified kaprekar numbers is a positive whole number with a special property. if you square it, then split the number into two integers and sum those integers, you have the same value you started with.
# consider a positive whole number n with d digits. we square n to arrive at a number that is either 2xd digits long or (2xd)-1 digits long. split the string representation of the square into two parts, l and r. the right hand part, r must be d digits long. the left is the remaining substring. convert those two substrings back to integers, add them and see if you get n.


import math
import os
import random
import re
import sys


def kaprekarNumbers(p, q):
    result = []
    for i in range(p, q+1):
        d = len(str(i))
        s = str(i**2)
        r = s[-d:]
        l = s[:-d]
        if l == '':
            l = 0
        if int(r) + int(l) == i:
            result.append(i)
    if result == []:
        print('INVALID RANGE')
    else:
        print(*result)  # * unpacks the list


p = int(input())
q = int(input())
result = kaprekarNumbers(p, q)
print(result)
