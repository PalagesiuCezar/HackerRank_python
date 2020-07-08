#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    note_ap, mag_ap = {},{}
    ok = 1

    #for small strings (crush on 2 tests)
    
    for i in note:
        if i in magazine and magazine.count(i) >= note.count(i):
            pass
        else:
            ok = 0
            break
    
    #for big strings (this works on every test)
    
    for i in note:
        if i not in note_ap:
            note_ap[i] = 1
        else:
            note_ap[i] += 1
    
    for i in magazine:
        if i not in mag_ap:
            mag_ap[i] = 1
        else:
            mag_ap[i] += 1
    
    for i in note_ap:
        if i in mag_ap and note_ap[i] <= mag_ap[i]:
            pass
        else:
            ok = 0
            break

    print('Yes') if ok else print('No')

if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)
