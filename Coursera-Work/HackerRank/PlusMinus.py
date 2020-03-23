import math
import os
import random
import re
import sys

# arr = list(map(int, input("Arrary: ").rstrip().split()))
# n = int(input("N: "))
arr = [-4, 3, -9, 0, 4, 1]
n = 6
# Complete the plusMinus function below.
def plusMinus(arr,n):
    # if __name__ == '__main__':
    pos = 0
    zero = 0
    neg = 0
    i = 0
    while i < len(arr):
        if arr[i] > 0:
            pos = pos +1
        elif arr[i] == 0:
            zero = zero +1
        elif arr[i] < 0:
            neg = neg +1
        i = i+1
    print(pos/(len(arr)))
    print(neg/(len(arr)))
    print(zero/(len(arr)))
    
    #return plusMinus(arr)
plusMinus(arr,n)