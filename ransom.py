# 6 4
# give me one grand today night
# give one grand today
# Sample Output 0
# Yes
# Sample Input 1
# 6 5
# two times three is not four
# two times two is four
# Sample Output 1
# No


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'checkMagazine' function below.
#
# The function accepts following parameters:
#  1. STRING_ARRAY magazine
#  2. STRING_ARRAY note
#

def checkMagazine(magazine, note):
    # Write your code here
    mag={}
    no ={}
    for i in range(len(magazine)):
        if magazine[i] not in mag:
            mag[magazine[i]] = 1
        else:
            mag[magazine[i]]+=1
    
    for i in range(len(note)):
        if note[i] not in no:
            no[note[i]] = 1
        else:
            no[note[i]]+=1
    
    for key, value in no.items():
        if key not in mag:
            print("No")
            return
        elif  no[key]>mag[key]:
            print("No")
            return
        
            
    print("Yes")
    return
            
            

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    m = int(first_multiple_input[0])

    n = int(first_multiple_input[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)
