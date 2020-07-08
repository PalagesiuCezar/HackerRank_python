#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    jumps,i = 0,0
   
    try:
        while i <= len(c)-3:
            if (c[i+1] == 1 and c[i+2] == 0) or (c[i+1] == 0 and c[i+2] == 0):
                i += 2
                jumps += 1
            elif c[i+1] == 0 and c[i+2] == 1:
                i += 1
                jumps +=1
            else:
                i += 1
                jumps += 1
    except IndexError:
        pass #just for program to not crush 
    
    if i == len(c)-1:
        return jumps
    return jumps+1  

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
