# There will be two arrays of integers. Determine all integers that satisfy the following two conditions:

# The elements of the first array are all factors of the integer being considered
# The integer being considered is a factor of all elements of the second array
# These numbers are referred to as being between the two arrays. Determine how many such numbers exist.

import math
import os
import random
import re
import sys


def getTotal(a, b):
    multiples_of_a = []
    factors_a = []

    final_integers = []
    total_length = len(a+b)

    for i in range(1, 101):
        for numbers_a in a:
            if i % numbers_a == 0:
                multiples_of_a.append(i)
        for numbers_b in b:
            if numbers_b % i == 0:
                factors_a.append(i)
        potential_integers = multiples_of_a + factors_a

    for number in potential_integers:
        if potential_integers.count(number) == total_length:
            final_integers.append(number)
    return len(set(final_integers))


a = [2, 6]
b = [24, 26]

result = getTotal(a, b)
print(result)
