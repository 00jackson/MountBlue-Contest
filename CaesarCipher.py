# Julius Caesar protected his confidential information by encrypting it using a cipher.
# Caesar's cipher shifts each letter by a number of letters. If the shift takes you past the end of the alphabet, just rotate back to the front of the alphabet.
# In the case of a rotation by 3, w, x, y and z would map to z, a, b and c.


import math
import os
import random
import re
import sys


def caesarCipher(s, k):
    n = len(s)
    temp = []

    for char in s:
        temp.append(ord(char))

    for i in range(n):
        # uppercase
        if 65 <= temp[i] <= 90:
            temp[i] = 65+(temp[i]+k-65) % 26
        # lowercase
        elif 97 <= temp[i] <= 122:
            temp[i] = 97+(temp[i]+k-97) % 26

    return "".join(map(chr, temp))


s = "middle-Outz"
k = 2
result = caesarCipher(s, k)
print(result)
