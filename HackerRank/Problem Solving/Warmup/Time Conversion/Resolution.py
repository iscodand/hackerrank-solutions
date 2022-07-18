#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    hours = s[:2] 
    minutes = s[3:5]
    seconds = s[6:8]
    
    indicator = s[8:]
    
    if indicator == 'PM' :
        if hours == '12':
            return s[:8]
        else: 
            hours = int(hours) + 12
            return f'{hours}:{minutes}:{seconds}'
    
    elif indicator == 'AM':
        if hours == '12':
            hours = '00'
            return f'{hours}:{minutes}:{seconds}'
        else:
            return s[:8]
    
    else:
        raise ValueError("Incorrect Format!")

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
