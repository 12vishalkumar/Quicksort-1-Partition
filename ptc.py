import math
import os
import random
import re
import sys
# Complete the 'quickSort' function below.
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
def quickSort(arr):
    # Write your code here
    left = []
    right = []
    equal = []
    p = arr[0]
    c = 1
    for i in range(1, len(arr)):
        if(p > arr[i]):
            left.append(arr[i])
        elif(p == arr[i]):
            c += 1
        else:
            right.append(arr[i])
    for i in range(c):
        equal.append(p)
    return (left + equal + right)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    result = quickSort(arr)
    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')
    fptr.close()
