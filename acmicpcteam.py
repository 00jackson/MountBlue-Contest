# there are a number of people who will be attending acm-icpc world finals. Each of them may be well versed in a number of topics. Given a list of topics known by each attendee, you must determine the maximum number of topics a 2-person team can know. Also find out how many ways a team can be formed to know that many topics. Lists will be in the form of bit strings, where each string represents an attendee and each position in that string represents a field of knowledge, 1 if its a known field or 0 if not.
# also determine the maximum number of topics a 2-person team can know by ORing together the known topics of each team member. Only consider teams where the number of topics known by each member is equal.


import math
import os
import random
import re
import sys


def acmicpcTeam(topic):
    count = 0
    maxSub = 0
    for i in range(n):
        for j in range(i+1, n):
            sub = 0
            for x, y in zip(topic[i], topic[i+1:]):
                if x == '1' or y == '1':
                    sub += 1
            if sub > maxSub:
                maxSub = sub
                count = 1
            elif sub == maxSub:
                count += 1
    return [maxSub, count]


n = int(input().strip())

m = int(input().strip())

topic = []

for _ in range(n):
    topic_item = input()
    topic.append(topic_item)

result = acmicpcTeam(topic)
print('\n'.join(map(str, result)))
