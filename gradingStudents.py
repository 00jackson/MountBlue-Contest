# - every student receives a grade in the inclusive range from 0 to 100.
# - any grade less than 40 is a failing grade.
# - Sam is a professor at the university and likes to round each student's grade according to these rules:
#    - if the difference between the grade and the next multiple of 5 is less than 3, round grade up to the next multiple of 5.
#    - if the value of grade is less than 38, no rounding occurs as the result will still be a failing grade.


import math
import os
import random
import re
import sys


def gradingStudents(grades):
    res = []
    for grade in grades:
        if grade >= 38:
            mod = grade % 5
            if mod >= 3:
                grade += (5 - mod)
        res.append(grade)
    return res


grades = [73, 67, 38, 33]
result = gradingStudents(grades)

print(result)
