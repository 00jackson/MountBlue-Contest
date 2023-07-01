# Two friends Anna and Brian, are deciding how to split the bill at a dinner. Each will only pay for the items they consume. Brian gets the check and calculates Anna's portion. You must determine if his calculation is correct.

import math
import os
import random
import re
import sys


def bonAppetit(bill, k, b):

    s = sum(bill)
    charge = (s - bill[k]) // 2

    if charge == b:
        print("Bon Appetit")
    else:
        print(b - charge)


bill = [3, 10, 2, 9]
k = 1
b = 12

bonAppetit(bill, k, b)
