#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pangrams' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def pangrams(s):
    string = s.lower();
    founded_chars = list();
    
    for char in string:
        if char not in founded_chars:
            founded_chars.append(char)
    
    #26 english lettters + 1 space char
    if len(founded_chars) != 27:
        return 'not pangram'
    else:
        return 'pangram'
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = pangrams(s)

    fptr.write(result + '\n')

    fptr.close()
