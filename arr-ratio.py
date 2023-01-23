#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    hasmap={"+":0,"-":0,"0":0}
    for i in range(len(arr)):
        if arr[i]==0:
            hasmap["0"]+=1
        if arr[i]>0:
            hasmap["+"]+=1
        if arr[i]<0:
            hasmap["-"]+=1
    print(round(hasmap["+"]/len(arr),6))
    print(round(hasmap["-"]/len(arr),6))
    print(round(hasmap["0"]/len(arr),6))
            

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
