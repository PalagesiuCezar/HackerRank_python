#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    nr = 0

    if s == 'a' and len(s) == 1:
        return n
    else:
        for i in range(n,len(s)-1,-1):
            if i%len(s) == 0:
                nr = int(i/len(s))
                break
    
    return (s.count('a')*nr + s[0:n-len(s)*nr].count('a'))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
