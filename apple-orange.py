#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countApplesAndOranges' function below.
#
# The function accepts following parameters:
#  1. INTEGER s
#  2. INTEGER t
#  3. INTEGER a
#  4. INTEGER b
#  5. INTEGER_ARRAY apples
#  6. INTEGER_ARRAY oranges
#

def countApplesAndOranges(s, t, a, b, apples, oranges):
    # Write your code here
    resultA=[]
    resultO=[]
    # print(apples,oranges)
    for i in range(len(apples)):
        resultA.append(apples[i]+a)
    for i in range(len(oranges)):
        resultO.append(oranges[i]+b)
    countA=0
    countO=0
    for i in range(len(resultA)):
        if(resultA[i]>=s and resultA[i]<=t):
            countA+=1
    for i in range(len(resultO)):       
        if(resultO[i]>=s and resultO[i]<=t):
            countO+=1
            
    print(countA)
    print(countO)
        

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    s = int(first_multiple_input[0])

    t = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    a = int(second_multiple_input[0])

    b = int(second_multiple_input[1])

    third_multiple_input = input().rstrip().split()

    m = int(third_multiple_input[0])

    n = int(third_multiple_input[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
