#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    alf = {}
    pairs = 0
    for i in range(0,len(ar)):
        if ar[i] in alf:
            alf[ar[i]] += 1
        else:
            alf[ar[i]] = 1
    for i in alf.values():
        if i%2==0:
            pairs += i/2
        else:
            pairs += (i-1)/2

    return int(pairs)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
