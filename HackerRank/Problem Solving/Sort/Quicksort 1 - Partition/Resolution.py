#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'quickSort' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def quickSort(arr):
    # Write your code here
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr.pop()
    
    items_greater = list()
    items_lower = list()
    
    for item in arr:
        if item > pivot:
            items_greater.append(item)
        else:
            items_lower.append(item)
        
    return quickSort(items_lower) + [pivot] + quickSort(items_greater)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = quickSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
