#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'marsExploration' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def marsExploration(s):
    # Write your code here
    counter = 0
    # Iteramos de 3 en 3 usando range
    for i in range(0, len(s), 3):
        # Aseguramos que haya un grupo completo de 3 letras para
        if i + 2 < len(s):
            
            if s[i] != 'S': counter += 1
            if s[i + 1] != 'O': counter += 1
            if s[i + 2] != 'S': counter += 1

    return counter

if __name__ == '__main__':
    output_path = os.environ.get('OUTPUT_PATH')
    fptr = open(output_path, 'w') if output_path else sys.stdout

    s = input().strip()

    result = marsExploration(s)

    fptr.write(str(result) + '\n')

    if output_path:
        fptr.close()
    
   