# A Discrete Mathematics professor has a class of students. Frustrated with their lack of discipline, the professor decides to cancel class if fewer than some number of students are present when class starts.
# Arrival times go from on time (arrivalTime <= 0) to arrived late (arrivalTime > 0).
# Given the arrival time of each student and a threshhold number of attendees, determine if the class is cancelled.

import math
import os
import random
import re
import sys


def angryProfessor(k, a):
    count = 0
    for i in a:
        if i <= 0:
            count += 1
    if count >= k:
        return 'NO'
    else:
        return 'YES'


k = 3
a = [-1, -3, 4, 2]

result = angryProfessor(k, a)
print(result)
