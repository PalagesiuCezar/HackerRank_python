#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    valley,sea_lvl = 0,0
    for it in s:
        if it == 'U':
            sea_lvl += 1
        else:
            sea_lvl -= 1
        if sea_lvl == 0 and it == 'U':
            valley +=1

    return valley

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
