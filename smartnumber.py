# in this challenge, the task is to debug the existing the existing code to successfully execute all provided test files.
# a number is called a smart number if it has an odd number of factors. given some numbers, find whether they are smart numbers or not.
# debug the given function is_smart_number to correctly check if a given number is a smart number.
#  Note: you can modify only one line in the given code and you cannot add or remove any new lines. To restore the original code, click on the icon to the right of th editor panel.

import math


def smartnumber(num):
    val = int(math.sqrt(num))
    if num / val == val:
        return True
    return False


for _ in range(int(input())):
    num = int(input())
    ans = smartnumber(num)
    if ans:
        print("YES")
    else:
        print("NO")
