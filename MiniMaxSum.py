#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    length = len(arr)
    sorted_array = sorted(arr)
    min_sum = 0
    max_sum = 0
    
    for number in sorted_array[0:length-1]:
        min_sum += number
    
    for number in sorted_array[length-4:]:
        max_sum += number
        
    print(min_sum , max_sum)

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
