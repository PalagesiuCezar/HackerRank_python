#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the twoStrings function below.
def twoStrings(s1, s2):
    ok = 0
    n = len(s1) if len(s1) < len(s2) else len(s2)   #just to take the smallest string if the difference between strings is huge
    for i in range(0,n):
        if n == len(s1):
            if s1[i] in s2:
                ok = 1
                break
            else:
                pass
        elif n == len(s2):
            if s2[i] in s1:
                ok = 1
                break
            else:
                pass

    return 'YES' if ok else 'NO'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s1 = input()

        s2 = input()

        result = twoStrings(s1, s2)

        fptr.write(result + '\n')

    fptr.close()
