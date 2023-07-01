# two players called p1 and p2 are playing a game with a starting number of stones. player 1 always plays first, and the two players move in alternating turns. the game's rules are as follows:
# - in a single move, a player can remove either 2, 3, or 5 stones from the game board.
# - if a player is unable to make a move, that player loses the game.
# given the starting number of stones, find and print the name of the winner. p1 is named first and p2 is named second. each player plays optimally, meaning they will not make a move that causes them to lose the game if some better, winning move exists.
# for example number of stones, find the game's winner if both players play optimally.for example, if n=4, p1 can make the following:
# - player 1 can remove 2 or 3 stones leaving 2 or 1 stone on the board. if there are 2 stones left, player 2 removes them and wins. if there is 1 stone left, player 1 removes it, and wins. player 2 cannot make any more moves so player 1 wins. in this case, print player 1.

import math
import os
import random
import re
import sys


def gameOfStones(n):
    return 'First' if n % 7 > 1 else 'Second'


n = 8
Result = gameOfStones(n)

print(Result)
